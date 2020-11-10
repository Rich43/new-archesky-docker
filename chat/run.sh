#!/bin/bash
get_latest_release() {
  curl --silent "https://api.github.com/repos/$1/releases/latest" | # Get latest release from GitHub api
    grep '"tag_name":' |                                            # Get tag line
    sed -E 's/.*"([^"]+)".*/\1/'                                    # Pluck JSON value
}

docker login docker.pkg.github.com/rich43
CHAT_SERVER_RELEASE=`get_latest_release "Rich43/archesky-chat-server"` CHAT_CLIENT_RELEASE=`get_latest_release "Rich43/chat-client"` docker-compose up -d
