from __future__ import annotations

import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


def run_web_ui(agent_service, host: str = "127.0.0.1", port: int = 8000) -> None:
    html = (Path(__file__).resolve().parent / "web" / "index.html").read_text(
        encoding="utf-8"
    )

    class ChatHandler(BaseHTTPRequestHandler):
        def do_GET(self) -> None:
            if self.path in {"/", "/index.html"}:
                self._send_html(html)
                return

            if self.path == "/history":
                self._send_json({"history": agent_service.get_history()})
                return

            self._send_json({"error": "未找到页面。"}, status=404)

        def do_POST(self) -> None:
            if self.path != "/chat":
                self._send_json({"error": "未找到接口。"}, status=404)
                return

            body = self._read_json()
            user_input = str(body.get("message", "")).strip()
            if not user_input:
                self._send_json({"error": "请输入指令。"}, status=400)
                return

            try:
                history = agent_service.submit(user_input)
            except Exception as exc:
                self._send_json({"error": str(exc)}, status=500)
                return

            self._send_json({"history": history})

        def log_message(self, format: str, *args) -> None:
            return

        def _read_json(self) -> dict:
            length = int(self.headers.get("Content-Length", "0"))
            raw_body = self.rfile.read(length).decode("utf-8") if length else "{}"
            return json.loads(raw_body or "{}")

        def _send_html(self, content: str) -> None:
            payload = content.encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(payload)))
            self.end_headers()
            self.wfile.write(payload)

        def _send_json(self, data: dict, status: int = 200) -> None:
            payload = json.dumps(data, ensure_ascii=False).encode("utf-8")
            self.send_response(status)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(payload)))
            self.end_headers()
            self.wfile.write(payload)

    server = ThreadingHTTPServer((host, port), ChatHandler)
    print(f"浏览器访问：http://{host}:{port}")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n服务已停止。")
    finally:
        server.server_close()
