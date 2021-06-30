# Generated by Snowball 2.1.0 - https://snowballstem.org/

from .basestemmer import BaseStemmer
from .among import Among


class SpanishStemmer(BaseStemmer):
    '''
    This class implements the stemming algorithm defined by a snowball script.
    Generated by Snowball 2.1.0 - https://snowballstem.org/
    '''

    a_0 = [
        Among(u"", -1, 6),
        Among(u"\u00E1", 0, 1),
        Among(u"\u00E9", 0, 2),
        Among(u"\u00ED", 0, 3),
        Among(u"\u00F3", 0, 4),
        Among(u"\u00FA", 0, 5)
    ]

    a_1 = [
        Among(u"la", -1, -1),
        Among(u"sela", 0, -1),
        Among(u"le", -1, -1),
        Among(u"me", -1, -1),
        Among(u"se", -1, -1),
        Among(u"lo", -1, -1),
        Among(u"selo", 5, -1),
        Among(u"las", -1, -1),
        Among(u"selas", 7, -1),
        Among(u"les", -1, -1),
        Among(u"los", -1, -1),
        Among(u"selos", 10, -1),
        Among(u"nos", -1, -1)
    ]

    a_2 = [
        Among(u"ando", -1, 6),
        Among(u"iendo", -1, 6),
        Among(u"yendo", -1, 7),
        Among(u"\u00E1ndo", -1, 2),
        Among(u"i\u00E9ndo", -1, 1),
        Among(u"ar", -1, 6),
        Among(u"er", -1, 6),
        Among(u"ir", -1, 6),
        Among(u"\u00E1r", -1, 3),
        Among(u"\u00E9r", -1, 4),
        Among(u"\u00EDr", -1, 5)
    ]

    a_3 = [
        Among(u"ic", -1, -1),
        Among(u"ad", -1, -1),
        Among(u"os", -1, -1),
        Among(u"iv", -1, 1)
    ]

    a_4 = [
        Among(u"able", -1, 1),
        Among(u"ible", -1, 1),
        Among(u"ante", -1, 1)
    ]

    a_5 = [
        Among(u"ic", -1, 1),
        Among(u"abil", -1, 1),
        Among(u"iv", -1, 1)
    ]

    a_6 = [
        Among(u"ica", -1, 1),
        Among(u"ancia", -1, 2),
        Among(u"encia", -1, 5),
        Among(u"adora", -1, 2),
        Among(u"osa", -1, 1),
        Among(u"ista", -1, 1),
        Among(u"iva", -1, 9),
        Among(u"anza", -1, 1),
        Among(u"log\u00EDa", -1, 3),
        Among(u"idad", -1, 8),
        Among(u"able", -1, 1),
        Among(u"ible", -1, 1),
        Among(u"ante", -1, 2),
        Among(u"mente", -1, 7),
        Among(u"amente", 13, 6),
        Among(u"aci\u00F3n", -1, 2),
        Among(u"uci\u00F3n", -1, 4),
        Among(u"ico", -1, 1),
        Among(u"ismo", -1, 1),
        Among(u"oso", -1, 1),
        Among(u"amiento", -1, 1),
        Among(u"imiento", -1, 1),
        Among(u"ivo", -1, 9),
        Among(u"ador", -1, 2),
        Among(u"icas", -1, 1),
        Among(u"ancias", -1, 2),
        Among(u"encias", -1, 5),
        Among(u"adoras", -1, 2),
        Among(u"osas", -1, 1),
        Among(u"istas", -1, 1),
        Among(u"ivas", -1, 9),
        Among(u"anzas", -1, 1),
        Among(u"log\u00EDas", -1, 3),
        Among(u"idades", -1, 8),
        Among(u"ables", -1, 1),
        Among(u"ibles", -1, 1),
        Among(u"aciones", -1, 2),
        Among(u"uciones", -1, 4),
        Among(u"adores", -1, 2),
        Among(u"antes", -1, 2),
        Among(u"icos", -1, 1),
        Among(u"ismos", -1, 1),
        Among(u"osos", -1, 1),
        Among(u"amientos", -1, 1),
        Among(u"imientos", -1, 1),
        Among(u"ivos", -1, 9)
    ]

    a_7 = [
        Among(u"ya", -1, 1),
        Among(u"ye", -1, 1),
        Among(u"yan", -1, 1),
        Among(u"yen", -1, 1),
        Among(u"yeron", -1, 1),
        Among(u"yendo", -1, 1),
        Among(u"yo", -1, 1),
        Among(u"yas", -1, 1),
        Among(u"yes", -1, 1),
        Among(u"yais", -1, 1),
        Among(u"yamos", -1, 1),
        Among(u"y\u00F3", -1, 1)
    ]

    a_8 = [
        Among(u"aba", -1, 2),
        Among(u"ada", -1, 2),
        Among(u"ida", -1, 2),
        Among(u"ara", -1, 2),
        Among(u"iera", -1, 2),
        Among(u"\u00EDa", -1, 2),
        Among(u"ar\u00EDa", 5, 2),
        Among(u"er\u00EDa", 5, 2),
        Among(u"ir\u00EDa", 5, 2),
        Among(u"ad", -1, 2),
        Among(u"ed", -1, 2),
        Among(u"id", -1, 2),
        Among(u"ase", -1, 2),
        Among(u"iese", -1, 2),
        Among(u"aste", -1, 2),
        Among(u"iste", -1, 2),
        Among(u"an", -1, 2),
        Among(u"aban", 16, 2),
        Among(u"aran", 16, 2),
        Among(u"ieran", 16, 2),
        Among(u"\u00EDan", 16, 2),
        Among(u"ar\u00EDan", 20, 2),
        Among(u"er\u00EDan", 20, 2),
        Among(u"ir\u00EDan", 20, 2),
        Among(u"en", -1, 1),
        Among(u"asen", 24, 2),
        Among(u"iesen", 24, 2),
        Among(u"aron", -1, 2),
        Among(u"ieron", -1, 2),
        Among(u"ar\u00E1n", -1, 2),
        Among(u"er\u00E1n", -1, 2),
        Among(u"ir\u00E1n", -1, 2),
        Among(u"ado", -1, 2),
        Among(u"ido", -1, 2),
        Among(u"ando", -1, 2),
        Among(u"iendo", -1, 2),
        Among(u"ar", -1, 2),
        Among(u"er", -1, 2),
        Among(u"ir", -1, 2),
        Among(u"as", -1, 2),
        Among(u"abas", 39, 2),
        Among(u"adas", 39, 2),
        Among(u"idas", 39, 2),
        Among(u"aras", 39, 2),
        Among(u"ieras", 39, 2),
        Among(u"\u00EDas", 39, 2),
        Among(u"ar\u00EDas", 45, 2),
        Among(u"er\u00EDas", 45, 2),
        Among(u"ir\u00EDas", 45, 2),
        Among(u"es", -1, 1),
        Among(u"ases", 49, 2),
        Among(u"ieses", 49, 2),
        Among(u"abais", -1, 2),
        Among(u"arais", -1, 2),
        Among(u"ierais", -1, 2),
        Among(u"\u00EDais", -1, 2),
        Among(u"ar\u00EDais", 55, 2),
        Among(u"er\u00EDais", 55, 2),
        Among(u"ir\u00EDais", 55, 2),
        Among(u"aseis", -1, 2),
        Among(u"ieseis", -1, 2),
        Among(u"asteis", -1, 2),
        Among(u"isteis", -1, 2),
        Among(u"\u00E1is", -1, 2),
        Among(u"\u00E9is", -1, 1),
        Among(u"ar\u00E9is", 64, 2),
        Among(u"er\u00E9is", 64, 2),
        Among(u"ir\u00E9is", 64, 2),
        Among(u"ados", -1, 2),
        Among(u"idos", -1, 2),
        Among(u"amos", -1, 2),
        Among(u"\u00E1bamos", 70, 2),
        Among(u"\u00E1ramos", 70, 2),
        Among(u"i\u00E9ramos", 70, 2),
        Among(u"\u00EDamos", 70, 2),
        Among(u"ar\u00EDamos", 74, 2),
        Among(u"er\u00EDamos", 74, 2),
        Among(u"ir\u00EDamos", 74, 2),
        Among(u"emos", -1, 1),
        Among(u"aremos", 78, 2),
        Among(u"eremos", 78, 2),
        Among(u"iremos", 78, 2),
        Among(u"\u00E1semos", 78, 2),
        Among(u"i\u00E9semos", 78, 2),
        Among(u"imos", -1, 2),
        Among(u"ar\u00E1s", -1, 2),
        Among(u"er\u00E1s", -1, 2),
        Among(u"ir\u00E1s", -1, 2),
        Among(u"\u00EDs", -1, 2),
        Among(u"ar\u00E1", -1, 2),
        Among(u"er\u00E1", -1, 2),
        Among(u"ir\u00E1", -1, 2),
        Among(u"ar\u00E9", -1, 2),
        Among(u"er\u00E9", -1, 2),
        Among(u"ir\u00E9", -1, 2),
        Among(u"i\u00F3", -1, 2)
    ]

    a_9 = [
        Among(u"a", -1, 1),
        Among(u"e", -1, 2),
        Among(u"o", -1, 1),
        Among(u"os", -1, 1),
        Among(u"\u00E1", -1, 1),
        Among(u"\u00E9", -1, 2),
        Among(u"\u00ED", -1, 1),
        Among(u"\u00F3", -1, 1)
    ]

    g_v = [17, 65, 16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 17, 4, 10]

    I_p2 = 0
    I_p1 = 0
    I_pV = 0

    def __r_mark_regions(self):
        self.I_pV = self.limit
        self.I_p1 = self.limit
        self.I_p2 = self.limit
        v_1 = self.cursor
        try:
            try:
                v_2 = self.cursor
                try:
                    if not self.in_grouping(SpanishStemmer.g_v, 97, 252):
                        raise lab2()
                    try:
                        v_3 = self.cursor
                        try:
                            if not self.out_grouping(SpanishStemmer.g_v, 97, 252):
                                raise lab4()
                            if not self.go_out_grouping(SpanishStemmer.g_v, 97, 252):
                                raise lab4()
                            self.cursor += 1
                            raise lab3()
                        except lab4: pass
                        self.cursor = v_3
                        if not self.in_grouping(SpanishStemmer.g_v, 97, 252):
                            raise lab2()
                        if not self.go_in_grouping(SpanishStemmer.g_v, 97, 252):
                            raise lab2()
                        self.cursor += 1
                    except lab3: pass
                    raise lab1()
                except lab2: pass
                self.cursor = v_2
                if not self.out_grouping(SpanishStemmer.g_v, 97, 252):
                    raise lab0()
                try:
                    v_4 = self.cursor
                    try:
                        if not self.out_grouping(SpanishStemmer.g_v, 97, 252):
                            raise lab6()
                        if not self.go_out_grouping(SpanishStemmer.g_v, 97, 252):
                            raise lab6()
                        self.cursor += 1
                        raise lab5()
                    except lab6: pass
                    self.cursor = v_4
                    if not self.in_grouping(SpanishStemmer.g_v, 97, 252):
                        raise lab0()
                    if self.cursor >= self.limit:
                        raise lab0()
                    self.cursor += 1
                except lab5: pass
            except lab1: pass
            self.I_pV = self.cursor
        except lab0: pass
        self.cursor = v_1
        v_5 = self.cursor
        try:
            if not self.go_out_grouping(SpanishStemmer.g_v, 97, 252):
                raise lab7()
            self.cursor += 1
            if not self.go_in_grouping(SpanishStemmer.g_v, 97, 252):
                raise lab7()
            self.cursor += 1
            self.I_p1 = self.cursor
            if not self.go_out_grouping(SpanishStemmer.g_v, 97, 252):
                raise lab7()
            self.cursor += 1
            if not self.go_in_grouping(SpanishStemmer.g_v, 97, 252):
                raise lab7()
            self.cursor += 1
            self.I_p2 = self.cursor
        except lab7: pass
        self.cursor = v_5
        return True

    def __r_postlude(self):
        while True:
            v_1 = self.cursor
            try:
                self.bra = self.cursor
                among_var = self.find_among(SpanishStemmer.a_0)
                if among_var == 0:
                    raise lab0()
                self.ket = self.cursor
                if among_var == 1:
                    if not self.slice_from(u"a"):
                        return False
                elif among_var == 2:
                    if not self.slice_from(u"e"):
                        return False
                elif among_var == 3:
                    if not self.slice_from(u"i"):
                        return False
                elif among_var == 4:
                    if not self.slice_from(u"o"):
                        return False
                elif among_var == 5:
                    if not self.slice_from(u"u"):
                        return False
                else:
                    if self.cursor >= self.limit:
                        raise lab0()
                    self.cursor += 1
                continue
            except lab0: pass
            self.cursor = v_1
            break
        return True

    def __r_RV(self):
        if not self.I_pV <= self.cursor:
            return False
        return True

    def __r_R1(self):
        if not self.I_p1 <= self.cursor:
            return False
        return True

    def __r_R2(self):
        if not self.I_p2 <= self.cursor:
            return False
        return True

    def __r_attached_pronoun(self):
        self.ket = self.cursor
        if self.find_among_b(SpanishStemmer.a_1) == 0:
            return False
        self.bra = self.cursor
        among_var = self.find_among_b(SpanishStemmer.a_2)
        if among_var == 0:
            return False
        if not self.__r_RV():
            return False
        if among_var == 1:
            self.bra = self.cursor
            if not self.slice_from(u"iendo"):
                return False
        elif among_var == 2:
            self.bra = self.cursor
            if not self.slice_from(u"ando"):
                return False
        elif among_var == 3:
            self.bra = self.cursor
            if not self.slice_from(u"ar"):
                return False
        elif among_var == 4:
            self.bra = self.cursor
            if not self.slice_from(u"er"):
                return False
        elif among_var == 5:
            self.bra = self.cursor
            if not self.slice_from(u"ir"):
                return False
        elif among_var == 6:
            if not self.slice_del():
                return False

        else:
            if not self.eq_s_b(u"u"):
                return False
            if not self.slice_del():
                return False

        return True

    def __r_standard_suffix(self):
        self.ket = self.cursor
        among_var = self.find_among_b(SpanishStemmer.a_6)
        if among_var == 0:
            return False
        self.bra = self.cursor
        if among_var == 1:
            if not self.__r_R2():
                return False
            if not self.slice_del():
                return False

        elif among_var == 2:
            if not self.__r_R2():
                return False
            if not self.slice_del():
                return False

            v_1 = self.limit - self.cursor
            try:
                self.ket = self.cursor
                if not self.eq_s_b(u"ic"):
                    self.cursor = self.limit - v_1
                    raise lab0()
                self.bra = self.cursor
                if not self.__r_R2():
                    self.cursor = self.limit - v_1
                    raise lab0()
                if not self.slice_del():
                    return False

            except lab0: pass
        elif among_var == 3:
            if not self.__r_R2():
                return False
            if not self.slice_from(u"log"):
                return False
        elif among_var == 4:
            if not self.__r_R2():
                return False
            if not self.slice_from(u"u"):
                return False
        elif among_var == 5:
            if not self.__r_R2():
                return False
            if not self.slice_from(u"ente"):
                return False
        elif among_var == 6:
            if not self.__r_R1():
                return False
            if not self.slice_del():
                return False

            v_2 = self.limit - self.cursor
            try:
                self.ket = self.cursor
                among_var = self.find_among_b(SpanishStemmer.a_3)
                if among_var == 0:
                    self.cursor = self.limit - v_2
                    raise lab1()
                self.bra = self.cursor
                if not self.__r_R2():
                    self.cursor = self.limit - v_2
                    raise lab1()
                if not self.slice_del():
                    return False

                if among_var == 1:
                    self.ket = self.cursor
                    if not self.eq_s_b(u"at"):
                        self.cursor = self.limit - v_2
                        raise lab1()
                    self.bra = self.cursor
                    if not self.__r_R2():
                        self.cursor = self.limit - v_2
                        raise lab1()
                    if not self.slice_del():
                        return False

            except lab1: pass
        elif among_var == 7:
            if not self.__r_R2():
                return False
            if not self.slice_del():
                return False

            v_3 = self.limit - self.cursor
            try:
                self.ket = self.cursor
                if self.find_among_b(SpanishStemmer.a_4) == 0:
                    self.cursor = self.limit - v_3
                    raise lab2()
                self.bra = self.cursor
                if not self.__r_R2():
                    self.cursor = self.limit - v_3
                    raise lab2()
                if not self.slice_del():
                    return False

            except lab2: pass
        elif among_var == 8:
            if not self.__r_R2():
                return False
            if not self.slice_del():
                return False

            v_4 = self.limit - self.cursor
            try:
                self.ket = self.cursor
                if self.find_among_b(SpanishStemmer.a_5) == 0:
                    self.cursor = self.limit - v_4
                    raise lab3()
                self.bra = self.cursor
                if not self.__r_R2():
                    self.cursor = self.limit - v_4
                    raise lab3()
                if not self.slice_del():
                    return False

            except lab3: pass
        else:
            if not self.__r_R2():
                return False
            if not self.slice_del():
                return False

            v_5 = self.limit - self.cursor
            try:
                self.ket = self.cursor
                if not self.eq_s_b(u"at"):
                    self.cursor = self.limit - v_5
                    raise lab4()
                self.bra = self.cursor
                if not self.__r_R2():
                    self.cursor = self.limit - v_5
                    raise lab4()
                if not self.slice_del():
                    return False

            except lab4: pass
        return True

    def __r_y_verb_suffix(self):
        if self.cursor < self.I_pV:
            return False
        v_2 = self.limit_backward
        self.limit_backward = self.I_pV
        self.ket = self.cursor
        if self.find_among_b(SpanishStemmer.a_7) == 0:
            self.limit_backward = v_2
            return False
        self.bra = self.cursor
        self.limit_backward = v_2
        if not self.eq_s_b(u"u"):
            return False
        if not self.slice_del():
            return False

        return True

    def __r_verb_suffix(self):
        if self.cursor < self.I_pV:
            return False
        v_2 = self.limit_backward
        self.limit_backward = self.I_pV
        self.ket = self.cursor
        among_var = self.find_among_b(SpanishStemmer.a_8)
        if among_var == 0:
            self.limit_backward = v_2
            return False
        self.bra = self.cursor
        self.limit_backward = v_2
        if among_var == 1:
            v_3 = self.limit - self.cursor
            try:
                if not self.eq_s_b(u"u"):
                    self.cursor = self.limit - v_3
                    raise lab0()
                v_4 = self.limit - self.cursor
                if not self.eq_s_b(u"g"):
                    self.cursor = self.limit - v_3
                    raise lab0()
                self.cursor = self.limit - v_4
            except lab0: pass
            self.bra = self.cursor
            if not self.slice_del():
                return False

        else:
            if not self.slice_del():
                return False

        return True

    def __r_residual_suffix(self):
        self.ket = self.cursor
        among_var = self.find_among_b(SpanishStemmer.a_9)
        if among_var == 0:
            return False
        self.bra = self.cursor
        if among_var == 1:
            if not self.__r_RV():
                return False
            if not self.slice_del():
                return False

        else:
            if not self.__r_RV():
                return False
            if not self.slice_del():
                return False

            v_1 = self.limit - self.cursor
            try:
                self.ket = self.cursor
                if not self.eq_s_b(u"u"):
                    self.cursor = self.limit - v_1
                    raise lab0()
                self.bra = self.cursor
                v_2 = self.limit - self.cursor
                if not self.eq_s_b(u"g"):
                    self.cursor = self.limit - v_1
                    raise lab0()
                self.cursor = self.limit - v_2
                if not self.__r_RV():
                    self.cursor = self.limit - v_1
                    raise lab0()
                if not self.slice_del():
                    return False

            except lab0: pass
        return True

    def _stem(self):
        self.__r_mark_regions()
        self.limit_backward = self.cursor
        self.cursor = self.limit
        v_2 = self.limit - self.cursor
        self.__r_attached_pronoun()
        self.cursor = self.limit - v_2
        v_3 = self.limit - self.cursor
        try:
            try:
                v_4 = self.limit - self.cursor
                try:
                    if not self.__r_standard_suffix():
                        raise lab2()
                    raise lab1()
                except lab2: pass
                self.cursor = self.limit - v_4
                try:
                    if not self.__r_y_verb_suffix():
                        raise lab3()
                    raise lab1()
                except lab3: pass
                self.cursor = self.limit - v_4
                if not self.__r_verb_suffix():
                    raise lab0()
            except lab1: pass
        except lab0: pass
        self.cursor = self.limit - v_3
        v_5 = self.limit - self.cursor
        self.__r_residual_suffix()
        self.cursor = self.limit - v_5
        self.cursor = self.limit_backward
        v_6 = self.cursor
        self.__r_postlude()
        self.cursor = v_6
        return True


class lab0(BaseException): pass


class lab1(BaseException): pass


class lab2(BaseException): pass


class lab3(BaseException): pass


class lab4(BaseException): pass


class lab5(BaseException): pass


class lab6(BaseException): pass


class lab7(BaseException): pass
