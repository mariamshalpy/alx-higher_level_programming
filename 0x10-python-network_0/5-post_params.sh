#!/bin/bash
# takes in a URL, sends a POST
curl "$1" -sX POST -d "email=hr@mariam.com&subject=I will always be here for PLD"
