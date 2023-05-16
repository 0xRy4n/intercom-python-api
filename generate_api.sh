help () {
    echo "Usage: $0 <openapi-spec> <package-version>"
    echo "  openapi-spec: The path to the openapi spec file"
    echo "  package-version: The version of the package"
    exit 1
}

if [ -z "$1" ]; then
    echo "Missing openapi-spec"
    help
fi

openapi-generator-cli generate -g python -t templates -i $1 -o . --additional-properties=packageName=intercom_python_api,projectName=intercom-python-api,nonCompliantUseDiscriminatorIfCompositionFails=true,packageUrl=https://github.com/0xRy4n/intercom-python-api.git,packageVersion=$2,useNose=true --schema-mappings object=typing.Dict,array=typinDg.List --skip-validate-spec
