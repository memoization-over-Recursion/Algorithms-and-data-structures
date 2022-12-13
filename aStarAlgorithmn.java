import java.util.*;

class aStarAlgorithm {
    // heuristic = educated guess
    // informed search algorithmn
    // time complexity O( w * h * log( w * h ))
    // space complexity O( w * h )
    public int[][] aStar(int startRow, int startCol, int endRow, int endCol, int[][] graph) {
        List<List<Node>> nodes = initializeNode(graph);
        Node start = nodes.get(startRow).get(startCol);
        Node end = nodes.get(endRow).get(endCol);

        start.dFromStart = 0;
        start.estimated = calculateManhattenDistance(start, end);

        List<Node> nodesLeftToVisit = new ArrayList<Node>();
        nodesLeftToVisit.add(start);
        MinHeap nTV = new MinHeap(nodesLeftToVisit);
        while (!nTV.isEmpty()) {
            Node cur = nTV.remove();
            if (cur == end) {
                break;
            }
            List<Node> neighbours = getNeighbours(cur, nodes);

            for (Node neighbor : neighbours) {
                if (neighbor.value == 1) {
                    continue;
                }

                int tDisToNeigh = cur.dFromStart + 1;
                if (tDisToNeigh >= neighbor.dFromStart) {
                    continue;
                }
                neighbor.cameFrom = cur;
                neighbor.dFromStart = tDisToNeigh;
                neighbor.estimated = tDisToNeigh + calculateManhattenDistance(neighbor, end);

                if (!nTV.containsNode(neighbor)) {
                    nTV.insert(neighbor);

                } else {

                    nTV.update(neighbor);
                }
            }
        }

        return reconstructPath(end);
    }

    List<List<Node>> initializeNode(int[][] graph) {
        List<List<Node>> ns = new ArrayList<List<Node>>();

        for (int i = 0; i < graph.length; i++) {
            List<Node> nList = new ArrayList<Node>();
            ns.add(nList);
            for (int j = 0; j < graph[i].length; j++) {
                ns.get(i).add(new Node(i, j, graph[i][j]));
            }
        }
        return ns;
    }

    int calculateManhattenDistance(Node current, Node end) {
        int currentR = current.row;
        int currentC = current.col;
        int endR = end.row;
        int endC = end.col;

        return Math.abs(currentR - endR) + Math.abs(currentC - endC);
    }

    int[][] reconstructPath(Node endNode) {
        if (endNode.cameFrom == null) {
            return new int[][] {};
        }
        Node current = endNode;
        List<List<Integer>> path = new ArrayList<List<Integer>>();

        while (current != null) {
            List<Integer> nodesData = new ArrayList<Integer>();
            nodesData.add(current.row);
            nodesData.add(current.col);
            path.add(nodesData);
            current = current.cameFrom;
        }

        int[][] answer = new int[path.size()][2];
        for (int i = 0; i < path.size(); i++) {
            answer[i][0] = path.get(path.size() - 1 - i).get(0);
            answer[i][1] = path.get(path.size() - 1 - i).get(1);
        }

        return answer;
    }

    List<Node> getNeighbours(Node node, List<List<Node>> nodes) {
        List<Node> neighbours = new ArrayList<Node>();
        int numRows = nodes.size();
        int numCols = nodes.get(0).size();

        int row = node.row;
        int col = node.col;

        if (row < numRows - 1) {
            neighbours.add(nodes.get(row + 1).get(col));
        }
        if (row > 0) {
            neighbours.add(nodes.get(row - 1).get(col));
        }
        if (col < numCols - 1) {
            neighbours.add(nodes.get(row).get(col + 1));
        }
        if (col > 0) {
            neighbours.add(nodes.get(row).get(col - 1));
        }
        return neighbours;
    }
}

class Node {
    String id;
    int row;
    int col;
    int value;
    int dFromStart;
    int estimated;
    Node cameFrom;

    Node(int row, int col, int value) {
        this.id = String.valueOf(row) + "-" + String.valueOf(col);
        this.row = row;
        this.col = col;
        this.value = value;
        this.dFromStart = Integer.MAX_VALUE;
        this.estimated = Integer.MAX_VALUE;
        this.cameFrom = null;
    }
}

class MinHeap {
    List<Node> heap = new ArrayList<Node>();
    Map<String, Integer> pos = new HashMap<String, Integer>();

    public MinHeap(List<Node> array) {
        for (int i = 0; i < array.size(); i++) {
            Node nodeAtI = array.get(i);
            pos.put(nodeAtI.id, i);
        }
        heap = buildHeap(array);
    }

    // time complexity O(n)
    // space complexity O(1)
    public List<Node> buildHeap(List<Node> array) {
        int firstParent = (array.size() - 2) / 2;
        for (int current = firstParent; current >= 0; current--) {
            siftDown(current, array.size() - 1, array);
        }
        return array;

    }

    // time complexity O(log(n))
    // space complexity O(1)
    public void siftDown(int currentIdx, int endIdx, List<Node> ar) {
        int childOne = currentIdx * 2 + 1;
        while (childOne <= endIdx) {
            int childTwo = currentIdx * 2 + 2 <= endIdx ? currentIdx * 2 + 2 : -1;
            int idxToSwap;
            if (childTwo != -1 && ar.get(childTwo).estimated < heap.get(childOne).estimated) {
                idxToSwap = childTwo;
            } else {
                idxToSwap = childOne;
            }
            if (ar.get(idxToSwap).estimated < ar.get(currentIdx).estimated) {
                swap(idxToSwap, currentIdx);
                currentIdx = idxToSwap;
                childOne = currentIdx * 2 + 1;
            } else {
                return;
            }
        }
    }

    // time complexity O(log(n))
    // space complexity O(1)
    public void siftUp(int currentIdx) {
        int parentIdx = (currentIdx - 1) / 2;
        while (currentIdx > 0 && heap.get(currentIdx).estimated < heap.get(parentIdx).estimated) {
            swap(currentIdx, (currentIdx - 1) / 2);
            currentIdx = parentIdx;
            parentIdx = (currentIdx - 1) / 2;
        }
    }

    public Node remove() {
        if (isEmpty()) {
            return null;
        }
        swap(0, heap.size() - 1);
        Node valRemoved = heap.get(heap.size() - 1);
        heap.remove(heap.size() - 1);
        pos.remove(valRemoved.id);
        siftDown(0, heap.size() - 1, heap);
        return valRemoved;
    }

    public void insert(Node n) {
        heap.add(n);
        pos.put(n.id, heap.size() - 1);
        siftUp(heap.size() - 1);
    }

    public void swap(int a, int b) {
        pos.put(heap.get(a).id, b);
        pos.put(heap.get(b).id, a);
        Node temp = heap.get(b);
        heap.set(b, heap.get(a));
        heap.set(a, temp);
    }

    public boolean isEmpty() {
        return heap.size() == 0;
    }

    public boolean containsNode(Node node) {
        return pos.containsKey(node.id);
    }

    public void update(Node node) {
        siftUp(pos.get(node.id));
    }
};
