import numpy as np
import itertools as it

P_LIMIT = 5


class Node:
    def __init__(self, xmin, xmax, ymin, ymax):
        self.particles = []
        self.children = None

        # delimiters for space represented by this node
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax

    def add(self, particle):
        if len(self.particles) < P_LIMIT:
            self.particles.add(particle)
        else:
            if not self.children:
                self.split()

    def split(self):
        ''' creates child nodes for quadrants '''
        xmid = (self.xmin + self.xmax) // 2
        ymid = (self.ymin + self.ymax) // 2
        ul = Node(self.xmin, xmid, self.ymin, ymid)
        ur = Node(xmid, self.xmax, self.ymin, ymid)
        lr = Node(xmid, self.xmax, ymid, self.ymax)
        ll = Node(self.xmin, xmid, ymid, self.ymax)
        self.children = [ul, ur, lr, ll]


class Quadtree:
    def __init__(self):
        self.root = None
        self.splitAt = None

    def add(self, particle):
        self.root.add(particle)

    def update(self, particle):
        pass


def colliding(p1, p2):
    ''' returns true if particles are colliding '''
    distance = np.linalg.norm(p1.coord - p2.coord)
    return p1.radius + p2.radius >= distance
