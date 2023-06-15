"""
Intercom tends not to adhere perfectly to it's own schema definitions for API responses.
Because the point of codegen is lazy client creation, we aren't going to bother fixing this.
Instead, we'll just remove the response schemas. Genius!
"""

import sys
import requests
import yaml

if __name__ == "__main__":
    spec_version = sys.argv[1]

    # Fetch the OpenAPI spec
    response = requests.get(f"https://raw.githubusercontent.com/intercom/Intercom-OpenAPI/main/descriptions/{spec_version}/api.intercom.io.yaml")

    if not response.ok:
        raise ValueError("Invalid specification version- could not find on 'intercom/Intercom-OpenAPI' repository.")

    spec = yaml.safe_load(response.text)

    for path, path_item in spec['paths'].items():
        # Iterate through the operations in each path (get, put, post, delete, etc.)
        for operation, operation_item in path_item.items():
            # If there are responses defined for the operation, modify them
            if 'responses' in operation_item:
                for response, response_item in operation_item['responses'].items():
                    if 'content' in response_item:
                        for content_type, content_item in response_item['content'].items():
                            if 'schema' in content_item:
                                # If the schema is not already an 'object', add 'object' as an additional acceptable schema
                                if 'type' in content_item['schema'] and content_item['schema']['type'] != 'object':
                                    content_item['schema'] = {
                                        'oneOf': [
                                            content_item['schema'],
                                            {'type': 'object'}
                                        ]
                                    }
                                # If there's no 'type' field, assume it's a complex schema and just add 'object' as an option
                                elif 'type' not in content_item['schema']:
                                    content_item['schema'] = {
                                        'oneOf': [
                                            content_item['schema'],
                                            {'type': 'object'}
                                        ]
                                    }

    # Convert the modified spec back to YAML
    modified_spec = yaml.safe_dump(spec)

    # Now, you can write the modified specification to a new file
    with open('spec.yaml', 'w') as file:
        file.write(modified_spec)