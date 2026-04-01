class Solution:
    def simplifyPath(self, path: str) -> str:
        """Return the canonical Unix path for an absolute
        input path.

        Treat "." as the current directory, ".." as the
        parent directory, and repeated slashes as a single
        separator. Sequences of periods other than "." and
        ".." count as normal path segments. The result must
        start with "/", use exactly one slash between
        segments, omit a trailing slash unless the result is
        the root directory, and contain no "." or ".."
        navigation segments. """
        path_segments = path.split("/")
        path_segments = [path_segment 
                         for path_segment in path_segments
                         if (path_segment != "." and
                             path_segment != "")]
        simplified_path = []
        for i in range(len(path_segments)):
            if path_segments[i] != "..":
                simplified_path += [path_segments[i]]
            elif simplified_path:
                simplified_path.pop()
        return "/" + "/".join(simplified_path)


if __name__ == "__main__":
    sol = Solution()
    samples = [
        ("/home/", "/home"),
        ("/home//foo/", "/home/foo"),
        ("/home/user/Documents/../Pictures", "/home/user/Pictures"),
        ("/../", "/"),
        ("/.../a/../b/c/../d/./", "/.../b/d"),
    ]

    for path, expected in samples:
        print("Input:", path)
        print("Expected:", expected)
        try:
            actual = sol.simplifyPath(path)
            print("Actual:", actual)
            print("Matches expected:", actual == expected)
        except NotImplementedError as exc:
            print("Actual: not implemented")
            print("Matches expected: False")
            print("Note:", exc)
        print()
