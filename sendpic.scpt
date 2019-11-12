on run argv
  tell application "Messages"
    set targetService to 1st service whose service type = iMessage
    set myid to item 2 of argv
    set mypath to item 1 of argv
    set ImageAttachment to POSIX file mypath as alias
    set theBuddy to a reference to buddy myid of targetService
    send ImageAttachment to theBuddy
  end tell
end run
