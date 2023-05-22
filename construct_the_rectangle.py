class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        '''
        Given a specific rectangular web page’s area, return rectangular,
        whose length L and width W satisfy the following requirements:
        
            The area of the rectangular web page you designed must equal to the given target area.
            The width W should not be larger than the length L, which means L >= W.
            The difference between length L and width W should be as small as possible.

        Return an array [L, W] where L and W are the length and
        width of the web page you designed in sequence.
        '''
        possible_areas = [[area // i, i] for i in range(1, int(area ** 0.5) + 2) if i <= area / i and area // i == area / i]
        if not possible_areas:
            return [area, 1]
        b = list(map(lambda x: x[0] - x[1], possible_areas))
        return possible_areas[b.index(min(b))]