#!/bin/bash

COMMAND=$1

OPT_STORE=false
OPT_EMAIL=false

while test -n "$1"; do
   case "$1" in
      --store|-s)
         OPT_STORE=true
         shift
         ;;
      --email|-e)
         OPT_EMAIL=true
         shift
         ;;
      *) 
        shift
        ;;
   esac
done

case "$COMMAND" in 
    clear )
        ;;
        
    analyze )
        ;;
        
    all )
        ;;
esac
