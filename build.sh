get_build_deps() {
    GT=1740607841

    curl -O https://raw.githubusercontent.com/cvsschaitanya/mediaremote-client/releases/build.${GT}.zip

    unzip -oq build.${GT}.zip -d ./client
}

./setup_venv.sh
. ./activate
get_build_deps

pyinstaller mediaremote.spec

