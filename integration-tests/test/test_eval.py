import os

from .rnode import (
    Node,
)


def test_eval(started_standalone_bootstrap_node: Node) -> None:
    relative_paths = started_standalone_bootstrap_node.shell_out('sh', '-c', 'ls /opt/docker/examples/*.rho').splitlines()
    for relative_path in relative_paths:
        full_path = os.path.join('/opt/docker/examples', relative_path)
        started_standalone_bootstrap_node.eval(full_path)
