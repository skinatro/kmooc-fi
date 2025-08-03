#!/bin/bash

retrieve_url(){
    url=$(curl -I -L --max-redirs 0 https://en.wikipedia.org/wiki/Special:Random | grep -i 'location' | awk '{print $2}' | tr -d '\r')
    echo "Random wiki URL is: $url"
}

retrieve_url
