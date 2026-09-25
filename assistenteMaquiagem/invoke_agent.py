import boto3
import uuid


HARNESS_ARN = "arn:aws:bedrock-agentcore:us-east-1:650830975368:harness/assistenteMaquiagem_assistenteMaquiagem-DRkvjFCIEP"


def perguntar_agentcore(pergunta, session_id=None):
    client = boto3.client(
        "bedrock-agentcore",
        region_name="us-east-1"
    )

    response = client.invoke_harness(
        harnessArn=HARNESS_ARN,
        runtimeSessionId=session_id or str(uuid.uuid4()),
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "text": pergunta
                    }
                ]
            }
        ]
    )

    resposta = ""

    for event in response["stream"]:

        if "contentBlockDelta" in event:
            delta = event["contentBlockDelta"].get("delta", {})

            if "text" in delta:
                resposta += delta["text"]

        elif "runtimeClientError" in event:
            raise RuntimeError(
                event["runtimeClientError"]["message"]
            )

       

    return resposta

  