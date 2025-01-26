class Solution: 
    def get_max_cycle_length(self, favorite: List[int]) -> int:
        person_cnt = len(favorite)
        max_cycle_length = 0

        seen = set()

        # for each person
        for i in range(person_cnt):
            # i - person i

            # if person not part of any chain (chain with cycle)
            if i in seen:
                continue
            
            # begin of chain (chain with cycle)
            begin_person = i

            # visited nodes inside of chain (chain with cycle)
            cur_visited = set()

            # cur_person
            cur_person = i

            # try to build chain with cycle
            while cur_person not in seen:
                seen.add(cur_person)
                cur_visited.add(cur_person)
                cur_person = favorite[cur_person]
            
            # if cycle exists
            if cur_person in cur_visited:
                # length of chain with cycle
                visited_person_cnt = len(cur_visited)

                # try to find length of cycle
                while begin_person != cur_person:
                    visited_person_cnt -= 1
                    begin_person = favorite[begin_person]
            
                max_cycle_length = max(max_cycle_length, visited_person_cnt)
        
        return max_cycle_length
    
    def get_max_chain_without_cycle_length(self, favorite: List[int]) -> int:
        person_cnt = len(favorite)
        max_chain_len = 0

        # find mutal-favorite (a <-> b) pairs
        pairs = []
        visited = set()

        for i in range(person_cnt):
            if i not in visited and favorite[favorite[i]] == i:
                pairs.append((i, favorite[i]))
                visited.add(i)
                visited.add(favorite[i])

        # build deps list, list that consits from deps from i (a -> b and c -> b, we shoul build such list [a,c] for b)
        deps = collections.defaultdict(list)
        for i in range(person_cnt):
            deps[favorite[i]].append(i)

        for src, dst in pairs:
            # max chain length to src
            max_dist_to_src = 0
            
            q = collections.deque()
            for dep in deps[src]:
                if dep != dst: q.append((dep, 1)) # dependent node and dist to dependent node
            
            while q:
                cur_dependency, dist = q.popleft()
                max_dist_to_src = max(max_dist_to_src, dist)
                for next_dep in deps[cur_dependency]:
                    q.append((next_dep, dist + 1))
            
            max_dist_to_dst = 0
            q = collections.deque()
            for dep in deps[dst]:
                if dep != src: q.append((dep, 1))
            
            while q:
                cur_dependency, dist = q.popleft()
                max_dist_to_dst = max(max_dist_to_dst, dist)
                for next_dep in deps[cur_dependency]:
                    q.append((next_dep, dist + 1)) 

            max_chain_len += 2 + max_dist_to_src + max_dist_to_dst

        return max_chain_len

    def maximumInvitations(self, favorite: List[int]) -> int:
        return max(self.get_max_cycle_length(favorite), self.get_max_chain_without_cycle_length(favorite))