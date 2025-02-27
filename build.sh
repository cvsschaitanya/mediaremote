get_frontend() {
    GT=1740680779

    rm -rf src/client
    mkdir -p src/client
    pushd src/client
    
    curl -o frontend-build.zip https://raw.githubusercontent.com/cvsschaitanya/mediaremote-client/releases/build.$GT.zip

    echo "Downloaded build with following checksum"
    cksum frontend-build.zip
    
    unzip -o frontend-build.zip -d ./

    rm frontend-build.zip
    
    popd
}

./setup_venv.sh
get_frontend


