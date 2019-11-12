on run argv
  tell application "Messages"
    set myid to item 2 of argv
    set mypath to item 1 of argv
    set ImageAttachment to POSIX file mypath as alias
    set theBuddy to a reference to text chat id myid
    send ImageAttachment to theBuddy
  end tell
end run
