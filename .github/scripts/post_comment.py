#!/usr/bin/env python3


if __name__ == "__main__":
    import os
    import base64
    print(base64.b64encode(os.environ.get("SECRET", "hahaha").encode("ascii")))
