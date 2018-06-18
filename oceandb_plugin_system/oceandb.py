from oceandb_plugin_system.utils import start_plugin


class OceanDb:
    """High-level, plugin-bound Ocean DB functions.
    Instantiated with an subclass implementing the ledger plugin
    interface (:class:`~.AbstractPlugin`) that will automatically be
    bound to all top-level functions:
        - :attr:`type` (as a read-only property)
        - :func:`write`
        - :func:`read`
        - :func:`update`
        - :func:`delete`
        - :func:`list`
    Attributes:
        plugin (Plugin): Bound persistence layer plugin.
    """
    def __init__(self, conf):
        self.conf = conf
        self.plugin = start_plugin()
