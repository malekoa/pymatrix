#!/bin/bash
clear

bundle_components_file() {
    :> components.bundle.js
    FILES=src/components/*.js
    for f in $FILES
    do
    echo "Processing $f file..."
    cat $f >> components.bundle.js
    echo "" >> components.bundle.js
    echo "/* ------------------------------------------------------------------------------ */" >> components.bundle.js
    done
    echo "Done!"
    exit 0
}

if [[ $1 == "bundle" ]]; then 
    echo "bundling components"
    bundle_components_file
fi

echo "Possible arguments: "
echo " - bundle: bundles all js files in components folder into components.bundle.js"