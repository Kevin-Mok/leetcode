import importlib.util
from pathlib import Path
import unittest


MODULE_PATH = (
    Path(__file__).resolve().parents[1]
    / "binary-tree"
    / "94-binary-tree-inorder-traversal.py"
)


def load_solution_module(test_case: unittest.TestCase):
    spec = importlib.util.spec_from_file_location(
        "binary_tree_inorder_traversal_94", MODULE_PATH
    )
    module = importlib.util.module_from_spec(spec)
    if spec is None or spec.loader is None:
        test_case.fail("solution module spec should load")
    try:
        spec.loader.exec_module(module)
    except Exception as exc:  # pragma: no cover - exercised in the red phase
        test_case.fail(f"solution module should import cleanly: {exc}")
    return module


class InorderTraversalTests(unittest.TestCase):
    def test_inorder_traversal_handles_empty_tree(self):
        module = load_solution_module(self)
        self.assertEqual(module.Solution().inorderTraversal(None), [])

    def test_inorder_traversal_visits_left_root_right(self):
        module = load_solution_module(self)
        root = module.TreeNode(
            1,
            None,
            module.TreeNode(2, module.TreeNode(3), None),
        )
        self.assertEqual(module.Solution().inorderTraversal(root), [1, 3, 2])


if __name__ == "__main__":
    unittest.main()
