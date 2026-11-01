from collections import OrderedDict


class ResponseCache:
    def __init__(self, maxsize: int = 128) -> None:
        if maxsize < 1:
            raise ValueError("maxsize must be at least 1.")
        self.maxsize = maxsize
        self._responses: OrderedDict[str, str] = OrderedDict()

    def get(self, prompt: str) -> str | None:
        response = self._responses.get(prompt)
        if response is not None:
            self._responses.move_to_end(prompt)
        return response

    def set(self, prompt: str, response: str) -> None:
        self._responses[prompt] = response
        self._responses.move_to_end(prompt)
        if len(self._responses) > self.maxsize:
            self._responses.popitem(last=False)
