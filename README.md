# clau-timer-prompt
go to sleep and have a prompt ready for claude to execute on the cli
works both ways with and wihtout esc press:

python3 messageTimer -esc 1 HOURS MINUTES (escape the limit reached message) "MESSAGE"
python3 messageTimer HOURS MINUTES "MESSAGE" 

python3 messageTimer 0 1 "stay still and dont say nothing, you are under ransom"
python3 messageTimer -esc 4 4 20 "continue with the implementation"