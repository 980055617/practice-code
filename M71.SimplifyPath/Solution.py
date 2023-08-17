class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        fixedPath = []
        for elem in path:
            if fixedPath and elem == '..':
                fixedPath.pop()
            elif elem not in ['.','..','']:
                fixedPath.append(elem)

        return "/" + "/".join(fixedPath)

if __name__ == '__main__':
    path = "/home/"
    solution = Solution()
    print(solution.simplifyPath(path))
