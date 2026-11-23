from tree_aio import XmasTree
import uasyncio as asyncio

if __name__ == '__main__':
    tree = XmasTree()
    tree.drawTree(tree.np)
    try:
        asyncio.run(tree.main())
    except KeyboardInterrupt:
        print('Interrupted')
    finally:
        _ = asyncio.new_event_loop()