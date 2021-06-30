# Generated by Snowball 2.1.0 - https://snowballstem.org/

from .basestemmer import BaseStemmer
from .among import Among


class DanishStemmer(BaseStemmer):
    '''
    This class implements the stemming algorithm defined by a snowball script.
    Generated by Snowball 2.1.0 - https://snowballstem.org/
    '''

    a_0 = [
        Among(u"hed", -1, 1),
        Among(u"ethed", 0, 1),
        Among(u"ered", -1, 1),
        Among(u"e", -1, 1),
        Among(u"erede", 3, 1),
        Among(u"ende", 3, 1),
        Among(u"erende", 5, 1),
        Among(u"ene", 3, 1),
        Among(u"erne", 3, 1),
        Among(u"ere", 3, 1),
        Among(u"en", -1, 1),
        Among(u"heden", 10, 1),
        Among(u"eren", 10, 1),
        Among(u"er", -1, 1),
        Among(u"heder", 13, 1),
        Among(u"erer", 13, 1),
        Among(u"s", -1, 2),
        Among(u"heds", 16, 1),
        Among(u"es", 16, 1),
        Among(u"endes", 18, 1),
        Among(u"erendes", 19, 1),
        Among(u"enes", 18, 1),
        Among(u"ernes", 18, 1),
        Among(u"eres", 18, 1),
        Among(u"ens", 16, 1),
        Among(u"hedens", 24, 1),
        Among(u"erens", 24, 1),
        Among(u"ers", 16, 1),
        Among(u"ets", 16, 1),
        Among(u"erets", 28, 1),
        Among(u"et", -1, 1),
        Among(u"eret", 30, 1)
    ]

    a_1 = [
        Among(u"gd", -1, -1),
        Among(u"dt", -1, -1),
        Among(u"gt", -1, -1),
        Among(u"kt", -1, -1)
    ]

    a_2 = [
        Among(u"ig", -1, 1),
        Among(u"lig", 0, 1),
        Among(u"elig", 1, 1),
        Among(u"els", -1, 1),
        Among(u"l\u00F8st", -1, 2)
    ]

    g_c = [119, 223, 119, 1]

    g_v = [17, 65, 16, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 48, 0, 128]

    g_s_ending = [239, 254, 42, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 16]

    I_x = 0
    I_p1 = 0
    S_ch = ""

    def __r_mark_regions(self):
        self.I_p1 = self.limit
        v_1 = self.cursor
        c = self.cursor + 3
        if c > self.limit:
            return False
        self.cursor = c
        self.I_x = self.cursor
        self.cursor = v_1
        if not self.go_out_grouping(DanishStemmer.g_v, 97, 248):
            return False
        if not self.go_in_grouping(DanishStemmer.g_v, 97, 248):
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
        among_var = self.find_among_b(DanishStemmer.a_0)
        if among_var == 0:
            self.limit_backward = v_2
            return False
        self.bra = self.cursor
        self.limit_backward = v_2
        if among_var == 1:
            if not self.slice_del():
                return False

        else:
            if not self.in_grouping_b(DanishStemmer.g_s_ending, 97, 229):
                return False
            if not self.slice_del():
                return False

        return True

    def __r_consonant_pair(self):
        v_1 = self.limit - self.cursor
        if self.cursor < self.I_p1:
            return False
        v_3 = self.limit_backward
        self.limit_backward = self.I_p1
        self.ket = self.cursor
        if self.find_among_b(DanishStemmer.a_1) == 0:
            self.limit_backward = v_3
            return False
        self.bra = self.cursor
        self.limit_backward = v_3
        self.cursor = self.limit - v_1
        if self.cursor <= self.limit_backward:
            return False
        self.cursor -= 1
        self.bra = self.cursor
        if not self.slice_del():
            return False

        return True

    def __r_other_suffix(self):
        v_1 = self.limit - self.cursor
        try:
            self.ket = self.cursor
            if not self.eq_s_b(u"st"):
                raise lab0()
            self.bra = self.cursor
            if not self.eq_s_b(u"ig"):
                raise lab0()
            if not self.slice_del():
                return False

        except lab0: pass
        self.cursor = self.limit - v_1
        if self.cursor < self.I_p1:
            return False
        v_3 = self.limit_backward
        self.limit_backward = self.I_p1
        self.ket = self.cursor
        among_var = self.find_among_b(DanishStemmer.a_2)
        if among_var == 0:
            self.limit_backward = v_3
            return False
        self.bra = self.cursor
        self.limit_backward = v_3
        if among_var == 1:
            if not self.slice_del():
                return False

            v_4 = self.limit - self.cursor
            self.__r_consonant_pair()
            self.cursor = self.limit - v_4
        else:
            if not self.slice_from(u"l\u00F8s"):
                return False
        return True

    def __r_undouble(self):
        if self.cursor < self.I_p1:
            return False
        v_2 = self.limit_backward
        self.limit_backward = self.I_p1
        self.ket = self.cursor
        if not self.in_grouping_b(DanishStemmer.g_c, 98, 122):
            self.limit_backward = v_2
            return False
        self.bra = self.cursor
        self.S_ch = self.slice_to()
        if self.S_ch == '':
            return False
        self.limit_backward = v_2
        if not self.eq_s_b(self.S_ch):
            return False
        if not self.slice_del():
            return False

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
        v_5 = self.limit - self.cursor
        self.__r_undouble()
        self.cursor = self.limit - v_5
        self.cursor = self.limit_backward
        return True


class lab0(BaseException): pass