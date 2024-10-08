#!/usr/bin/env python3


if __name__ == "__main__":
    import os
    print([x for x in os.environ.get("SECRET", "hahaha")])
