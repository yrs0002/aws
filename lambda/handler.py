import json

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps('¡Hola desde GitHub Actions! Despliegue automático funcionando correctamente.')
    }