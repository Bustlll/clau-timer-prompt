# clau-timer-prompt

Run a timer and automatically send a prompt to **Claude** when the time is up.  
Perfect for starting a task while you're away or preparing a prompt before you wake up.

---

## Usage

### Basic syntax

```bash
python3 messageTimer HOURS MINUTES "MESSAGE"
```

### With escape flag

```bash
python3 messageTimer -esc ESCAPE_HOURS HOURS MINUTES "MESSAGE"
```

The `-esc` flag suppresses the **limit reached message** for a specified number of hours.

---

## Parameters

| Parameter | Description |
|-----------|-------------|
| `HOURS` | Number of hours to wait |
| `MINUTES` | Number of minutes to wait |
| `MESSAGE` | Prompt that will be sent to Claude |
| `-esc` | Optional flag to escape the limit-reached message |
| `ESCAPE_HOURS` | Duration (in hours) to suppress the limit message |

---

## Examples

### Basic timer

Wait **1 minute** and send a prompt:

```bash
python3 messageTimer 0 1 "stay still and dont say nothing, you are under ransom"
```

---

### Timer with escape flag

Wait **4 hours and 20 minutes**, then exit the limit message and send message:

```bash
python3 messageTimer -esc 4 4 20 "continue with the implementation"
```

---

## Use Cases

- Prepare prompts while sleeping
- Schedule long-running coding instructions, even multiple prompts
- Resume interrupted work automatically
- Queue prompts for AI workflows