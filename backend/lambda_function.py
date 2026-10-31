
import json
import boto3
from decimal import Decimal

# DynamoDB connection
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('EmployeeTable')


# Convert Decimal into JSON-compatible numbers
def decimal_default(obj):

    if isinstance(obj, Decimal):

        if obj % 1 == 0:
            return int(obj)

        return float(obj)

    raise TypeError(
        f"Object of type {type(obj).__name__} is not JSON serializable"
    )


# Standard HTTP response
def response(status_code, data):

    return {
        'statusCode': status_code,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps(data, default=decimal_default)
    }


# Lambda handler
def lambda_handler(event, context):

    try:

        # Read HTTP API Gateway request
        http = event.get('requestContext', {}).get('http', {})

        method = http.get('method', '').upper()

        path_params = event.get('pathParameters') or {}

        employee_id = path_params.get('employeeId')

        # Read request body
        body = event.get('body') or '{}'

        if event.get('isBase64Encoded'):
            return response(400, {
                'message': 'Base64 encoded body is not supported'
            })

        data = json.loads(body, parse_float=Decimal)

        # CREATE EMPLOYEE
        if method == 'POST' and http.get('path') == '/employees':

            employee = data

            if not employee.get('employeeId'):
                return response(400, {
                    'message': 'employeeId is required'
                })

            table.put_item(
                Item=employee,
                ConditionExpression='attribute_not_exists(employeeId)'
            )

            return response(201, {
                'message': 'Employee created successfully',
                'employee': employee
            })

        # LIST ALL EMPLOYEES
        elif method == 'GET' and not employee_id:

            result = table.scan()

            return response(200, {
                'employees': result.get('Items', [])
            })

        # GET SINGLE EMPLOYEE
        elif method == 'GET' and employee_id:

            result = table.get_item(
                Key={'employeeId': employee_id}
            )

            employee = result.get('Item')

            if not employee:
                return response(404, {
                    'message': 'Employee not found'
                })

            return response(200, employee)

        # UPDATE EMPLOYEE
        elif method == 'PUT' and employee_id:

            allowed_fields = [
                'employeeName',
                'department',
                'salary'
            ]

            updates = {
                key: value
                for key, value in data.items()
                if key in allowed_fields
            }

            if not updates:
                return response(400, {
                    'message': 'No valid employee fields provided'
                })

            expression_names = {}
            expression_values = {}
            update_parts = []

            for index, (key, value) in enumerate(updates.items()):

                name_token = f'#field{index}'
                value_token = f':value{index}'

                expression_names[name_token] = key
                expression_values[value_token] = value

                update_parts.append(
                    f'{name_token} = {value_token}'
                )

            result = table.update_item(
                Key={'employeeId': employee_id},
                UpdateExpression='SET ' + ', '.join(update_parts),
                ExpressionAttributeNames=expression_names,
                ExpressionAttributeValues=expression_values,
                ConditionExpression='attribute_exists(employeeId)',
                ReturnValues='ALL_NEW'
            )

            return response(200, {
                'message': 'Employee updated successfully',
                'employee': result['Attributes']
            })

        # DELETE EMPLOYEE
        elif method == 'DELETE' and employee_id:

            table.delete_item(
                Key={'employeeId': employee_id},
                ConditionExpression='attribute_exists(employeeId)'
            )

            return response(200, {
                'message': 'Employee deleted successfully',
                'employeeId': employee_id
            })

        else:

            return response(404, {
                'message': 'Unsupported route or HTTP method'
            })

    except dynamodb.meta.client.exceptions.ConditionalCheckFailedException:

        return response(404, {
            'message': 'Employee already exists or does not exist'
        })

    except json.JSONDecodeError:

        return response(400, {
            'message': 'Invalid JSON request body'
        })

    except Exception as e:

        print('Error:', str(e))

        return response(500, {
            'error': str(e)
        })
