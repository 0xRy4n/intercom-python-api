#!/bin/bash

PACKAGE_URL="https://github.com/0xRy4n/intercom-python-api,packageVersion=1.0.1,projectName=intercom-python-api"
package_version=$(cat ./docs/package_version)

# LOG FUNCTIONS

log () {
    echo "[*] $1"
}
error () {
    echo "[X] ERROR: $1" >&2
    exit
}

# GENERATIVE FUNCTIONS

increment_version() {
    major=$(echo $package_version | cut -d. -f1)
    minor=$(echo $package_version | cut -d. -f2)
    patch=$(echo $package_version | cut -d. -f3)

    if [[ $1 == "major" ]]; then
        major=$((major + 1))
        minor=0
        patch=0
    elif [[ $1 == "minor" ]]; then
        minor=$((minor + 1))
        patch=0
    elif [[ $1 == "patch" ]]; then
        patch=$((patch + 1))
    elif [ -z $1 ]; then
        patch=$((patch + 1))
    else
        echo "Invalid flag. Please use 'major', 'minor', or 'patch' or leave blank to default to patch."
        exit 1
    fi

    package_version="$major.$minor.$patch"
    echo $package_version
}

# PROGRAM

increment_version $1

log "Checking for uncommon required packages ..."

if ! command -v openapi-generator-cli &> /dev/null
then
    error "openapi-generator-cli could not be found. Please install it."
fi

if ! command -v jq &> /dev/null
then
    error "jq could not be found. Please install it."
fi

log "All packages found."

log "Getting OpenAPI specifications from official Intercom repository ..."
descriptions=$(curl -XGET --url 'https://api.github.com/repos/intercom/Intercom-OpenAPI/contents/descriptions')

log $descriptions
log "Parsing found specifications ..."

echo $descriptions | jq -c '.[]' | while read description;
do
    version="$(echo $description | jq .name | tr -d '"')"
    if [ $version = "0" ]
    then
        parsed_version="unstable"
    else
        parsed_version=$version
    fi

    log "Checking out git repository for branch $parsed_version"
    git checkout $parsed_version || git checkout -b $parsed_version

    log "Downloading spec file and generating code for API Version: $version"
    wget "https://raw.githubusercontent.com/intercom/Intercom-OpenAPI/main/descriptions/$version/api.intercom.io.yaml" -O /tmp/intercom_api.yaml

    if [ "$(md5sum /tmp/intercom_api.yaml)" = "$(md5sum docs/api.intercom.io.yaml)" ]
    then
        continue
    else
        mv /tmp/intercom_api.yaml docs/api.intercom.io.yaml
    fi

    echo $package_version > docs/package_version
    openapi-generator-cli generate -t templates -g python -o . -i docs/api.intercom.io.yaml --skip-validate-spec --additional-properties=packageName=intercom_python_api,packageUrl=$PACKAGE_URL,packageVersion=$package_version

    git add .
    git commit -m "Automated update of branch using update_repo.sh script."
    git push "origin/$parsed_version"

done

log "Update finished."





    

