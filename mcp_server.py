import sys
import json
from client import ChaseLevDeque

def main():
    deque = ChaseLevDeque()
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        req = json.loads(line)
        method = req.get("method")
        params = req.get("params", {})
        if method == "push":
            deque.push_bottom(params.get("task"))
            res = {"status": "ok"}
        elif method == "pop":
            t = deque.pop_bottom()
            res = {"task": t}
        elif method == "steal":
            t = deque.steal()
            res = {"task": t}
        else:
            res = {"error": "unknown method"}
        sys.stdout.write(json.dumps({"id": req.get("id"), "result": res}) + "\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
