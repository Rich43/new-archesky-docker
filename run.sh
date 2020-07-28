#!/bin/bash
get_latest_release() {
  curl --silent "https://api.github.com/repos/$1/releases/latest" | # Get latest release from GitHub api
    grep '"tag_name":' |                                            # Get tag line
    sed -E 's/.*"([^"]+)".*/\1/'                                    # Pluck JSON value
}

docker login docker.pkg.github.com/rich43
CONTENT_SERVER_RELEASE=`get_latest_release "Rich43/archesky-content-server"` AUTH_SERVER_RELEASE=`get_latest_release "Rich43/archesky-auth-server"` docker-compose up -d
