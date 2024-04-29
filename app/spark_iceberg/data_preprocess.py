from datetime import datetime
import json

def process_kafka_message(record):
    trace_data = []
    try:
        kafka_message = record.value
        resource_spans = kafka_message.get('resourceSpans', [])
        for resource_span in resource_spans:
            scope_spans = resource_span.get('scopeSpans', [])
            for scope_span in scope_spans:
                spans = scope_span.get('spans', [])
                for span in spans:
                    trace_id = span.get('traceId')
                    start_unix_nano_time = span.get('startTimeUnixNano')
                    created_time = datetime.utcfromtimestamp(int(start_unix_nano_time) / 1e9)
                    json_string = json.dumps(span)
                    trace_data.append({
                        "traceId": trace_id,
                        # "createdTime": created_time,
                        "logData": "mydata"
                    })
    except Exception as e:
        print("Error processing Kafka message:", str(e))
    return trace_data
