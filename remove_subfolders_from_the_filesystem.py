class Solution:
    def removeSubfolders(self, folder: list[str]) -> list[str]:
        """Removes all sub-folders from a list of folder paths.

        Given a list of folder paths, returns a list with all sub-folders removed.
        A folder is considered a sub-folder if it is contained within another folder
        in the list (i.e., its path starts with another folder's path followed by a '/').

        Args:
            folder (List[str]): List of folder paths as strings.

        Returns:
            List[str]: List of folder paths with all sub-folders removed.

        Example:
            >>> removeSubfolders(["/a","/a/b","/c/d","/c/d/e","/c/f"])
            ['/a', '/c/d', '/c/f']

        Time complexity: O(n log n), where n is the number of folders (due to sorting).
        Space complexity: O(n)

        LeetCode: Beats 94.36% of submissions
        """
        folder.sort()
        folders = [folder[0]]

        for f in folder:
            if not f.startswith(folders[-1]):
                folders.append(f)
            else:
                if len(f) > len(folders[-1]) and f[len(folders[-1])] != "/":
                    folders.append(f)

        return folders
