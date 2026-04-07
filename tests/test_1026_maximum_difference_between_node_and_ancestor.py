import importlib.util
from pathlib import Path
import unittest


MODULE_PATH = (
    Path(__file__).resolve().parents[1]
    / "binary-tree"
    / "1026-maximum-difference-between-node-and-ancestor.py"
)


def load_solution_module(test_case: unittest.TestCase):
    spec = importlib.util.spec_from_file_location(
        "maximum_difference_between_node_and_ancestor_1026",
        MODULE_PATH,
    )
    module = importlib.util.module_from_spec(spec)
    if spec is None or spec.loader is None:
        test_case.fail("solution module spec should load")
    try:
        spec.loader.exec_module(module)
    except Exception as exc:  # pragma: no cover - exercised in the red phase
        test_case.fail(f"solution module should import cleanly: {exc}")
    return module


class MinValuesTreeTests(unittest.TestCase):
    def test_min_values_tree_returns_leaf_value(self):
        module = load_solution_module(self)
        leaf = module.TreeNode(7)

        self.assertEqual(module.Solution().min_values_tree(leaf), 7)

    def test_min_values_tree_uses_smallest_descendant(self):
        module = load_solution_module(self)
        root = module.TreeNode(
            8,
            module.TreeNode(3, module.TreeNode(1), module.TreeNode(6)),
            module.TreeNode(10),
        )

        self.assertEqual(module.Solution().min_values_tree(root), 1)

    def test_min_values_tree_handles_single_right_branch(self):
        module = load_solution_module(self)
        root = module.TreeNode(5, None, module.TreeNode(4, None, module.TreeNode(2)))

        self.assertEqual(module.Solution().min_values_tree(root), 2)


class MaxValuesTreeTests(unittest.TestCase):
    def test_max_values_tree_returns_leaf_value(self):
        module = load_solution_module(self)
        leaf = module.TreeNode(7)

        self.assertEqual(module.Solution().max_values_tree(leaf), 7)

    def test_max_values_tree_uses_largest_descendant(self):
        module = load_solution_module(self)
        root = module.TreeNode(
            8,
            module.TreeNode(3, module.TreeNode(1), module.TreeNode(6)),
            module.TreeNode(10, None, module.TreeNode(14)),
        )

        self.assertEqual(module.Solution().max_values_tree(root), 14)

    def test_max_values_tree_handles_single_left_branch(self):
        module = load_solution_module(self)
        root = module.TreeNode(5, module.TreeNode(6, module.TreeNode(9)), None)

        self.assertEqual(module.Solution().max_values_tree(root), 9)


class MaxAncestorDiffTests(unittest.TestCase):
    def test_max_ancestor_diff_matches_example_one(self):
        module = load_solution_module(self)
        root = module.build_tree([8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13])

        self.assertEqual(module.Solution().maxAncestorDiff(root), 7)


if __name__ == "__main__":
    unittest.main()
