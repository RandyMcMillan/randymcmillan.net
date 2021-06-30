# Generated by Snowball 2.1.0 - https://snowballstem.org/

from .basestemmer import BaseStemmer
from .among import Among


class SwedishStemmer(BaseStemmer):
    '''
    This class implements the stemming algorithm defined by a snowball script.
    Generated by Snowball 2.1.0 - https://snowballstem.org/
    '''

    a_0 = [
        Among(u"a", -1, 1),
        Among(u"arna", 0, 1),
        Among(u"erna", 0, 1),
        Among(u"heterna", 2, 1),
        Among(u"orna", 0, 1),
        Among(u"ad", -1, 1),
        Among(u"e", -1, 1),
        Among(u"ade", 6, 1),
        Among(u"ande", 6, 1),
        Among(u"arne", 6, 1),
        Among(u"are", 6, 1),
        Among(u"aste", 6, 1),
        Among(u"en", -1, 1),
        Among(u"anden", 12, 1),
        Among(u"aren", 12, 1),
        Among(u"heten", 12, 1),
        Among(u"ern", -1, 1),
        Among(u"ar", -1, 1),
        Among(u"er", -1, 1),
        Among(u"heter", 18, 1),
        Among(u"or", -1, 1),
        Among(u"s", -1, 2),
        Among(u"as", 21, 1),
        Among(u"arnas", 22, 1),
        Among(u"ernas", 22, 1),
        Among(u"ornas", 22, 1),
        Among(u"es", 21, 1),
        Among(u"ades", 26, 1),
        Among(u"andes", 26, 1),
        Among(u"ens", 21, 1),
        Among(u"arens", 29, 1),
        Among(u"hetens", 29, 1),
        Among(u"erns", 21, 1),
        Among(u"at", -1, 1),
        Among(u"andet", -1, 1),
        Among(u"het", -1, 1),
        Among(u"ast", -1, 1)
    ]

    a_1 = [
        Among(u"dd", -1, -1),
        Among(u"gd", -1, -1),
        Among(u"nn", -1, -1),
        Among(u"dt", -1, -1),
        Among(u"gt", -1, -1),
        Among(u"kt", -1, -1),
        Among(u"tt", -1, -1)
    ]

    a_2 = [
        Among(u"ig", -1, 1),
        Among(u"lig", 0, 1),
        Among(u"els", -1, 1),
        Among(u"fullt", -1, 3),
        Among(u"l\u00F6st", -1, 2)
    ]

    g_v = [17, 65, 16, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 24, 0, 32]

    g_s_ending = [119, 127, 149]

    I_x = 0
    I_p1 = 0

    def __r_mark_regions(self):
        self.I_p1 = self.limit
        v_1 = self.cursor
        c = self.cursor + 3
        if c > self.limit:
            return False
        self.cursor = c
        self.I_x = self.cursor
        self.cursor = v_1
        if not self.go_out_grouping(SwedishStemmer.g_v, 97, 246):
            return False
        if not self.go_in_grouping(SwedishStemmer.g_v, 97, 246):
            return False
        self.cursor += 1
        self.I_p1 = self.cursor
        try:
            if not self.I_p1 < self.I_x:
                raise lab0()
            self.I_p1 = self.I_x
        except lab0: pass
        return True

    def __r_main_suffix(self):
        if self.cursor < self.I_p1:
            return False
        v_2 = self.limit_backward
        self.limit_backward = self.I_p1
        self.ket = self.cursor
        among_var = self.find_among_b(SwedishStemmer.a_0)
        if among_var == 0:
            self.limit_backward = v_2
            return False
        self.bra = self.cursor
        self.limit_backward = v_2
        if among_var == 1:
            if not self.slice_del():
                return False

        else:
            if not self.in_grouping_b(SwedishStemmer.g_s_ending, 98, 121):
                return False
            if not self.slice_del():
                return False

        return True

    def __r_consonant_pair(self):
        if self.cursor < self.I_p1:
            return False
        v_2 = self.limit_backward
        self.limit_backward = self.I_p1
        v_3 = self.limit - self.cursor
        if self.find_among_b(SwedishStemmer.a_1) == 0:
            self.limit_backward = v_2
            return False
        self.cursor = self.limit - v_3
        self.ket = self.cursor
        if self.cursor <= self.limit_backward:
            self.limit_backward = v_2
            return False
        self.cursor -= 1
        self.bra = self.cursor
        if not self.slice_del():
            return False

        self.limit_backward = v_2
        return True

    def __r_other_suffix(self):
        if self.cursor < self.I_p1:
            return False
        v_2 = self.limit_backward
        self.limit_backward = self.I_p1
        self.ket = self.cursor
        among_var = self.find_among_b(SwedishStemmer.a_2)
        if among_var == 0:
            self.limit_backward = v_2
            return False
        self.bra = self.cursor
        if among_var == 1:
            if not self.slice_del():
                return False

        elif among_var == 2:
            if not self.slice_from(u"l\u00F6s"):
                return False
        else:
            if not self.slice_from(u"full"):
                return False
        self.limit_backward = v_2
        return True

    def _stem(self):
        v_1 = self.cursor
        self.__r_mark_regions()
        self.cursor = v_1
        self.limit_backward = self.cursor
        self.cursor = self.limit
        v_2 = self.limit - self.cursor
        self.__r_main_suffix()
        self.cursor = self.limit - v_2
        v_3 = self.limit - self.cursor
        self.__r_consonant_pair()
        self.cursor = self.limit - v_3
        v_4 = self.limit - self.cursor
        self.__r_other_suffix()
        self.cursor = self.limit - v_4
        self.cursor = self.limit_backward
        return True


class lab0(BaseException): pass
