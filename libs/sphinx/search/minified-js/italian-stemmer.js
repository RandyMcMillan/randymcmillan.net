ItalianStemmer=function(){var r=new BaseStemmer;var e=[["",-1,7],["qu",0,6],["á",0,1],["é",0,2],["í",0,3],["ó",0,4],["ú",0,5]];var i=[["",-1,3],["I",0,1],["U",0,2]];var a=[["la",-1,-1],["cela",0,-1],["gliela",0,-1],["mela",0,-1],["tela",0,-1],["vela",0,-1],["le",-1,-1],["cele",6,-1],["gliele",6,-1],["mele",6,-1],["tele",6,-1],["vele",6,-1],["ne",-1,-1],["cene",12,-1],["gliene",12,-1],["mene",12,-1],["sene",12,-1],["tene",12,-1],["vene",12,-1],["ci",-1,-1],["li",-1,-1],["celi",20,-1],["glieli",20,-1],["meli",20,-1],["teli",20,-1],["veli",20,-1],["gli",20,-1],["mi",-1,-1],["si",-1,-1],["ti",-1,-1],["vi",-1,-1],["lo",-1,-1],["celo",31,-1],["glielo",31,-1],["melo",31,-1],["telo",31,-1],["velo",31,-1]];var s=[["ando",-1,1],["endo",-1,1],["ar",-1,2],["er",-1,2],["ir",-1,2]];var o=[["ic",-1,-1],["abil",-1,-1],["os",-1,-1],["iv",-1,1]];var u=[["ic",-1,1],["abil",-1,1],["iv",-1,1]];var t=[["ica",-1,1],["logia",-1,3],["osa",-1,1],["ista",-1,1],["iva",-1,9],["anza",-1,1],["enza",-1,5],["ice",-1,1],["atrice",7,1],["iche",-1,1],["logie",-1,3],["abile",-1,1],["ibile",-1,1],["usione",-1,4],["azione",-1,2],["uzione",-1,4],["atore",-1,2],["ose",-1,1],["ante",-1,1],["mente",-1,1],["amente",19,7],["iste",-1,1],["ive",-1,9],["anze",-1,1],["enze",-1,5],["ici",-1,1],["atrici",25,1],["ichi",-1,1],["abili",-1,1],["ibili",-1,1],["ismi",-1,1],["usioni",-1,4],["azioni",-1,2],["uzioni",-1,4],["atori",-1,2],["osi",-1,1],["anti",-1,1],["amenti",-1,6],["imenti",-1,6],["isti",-1,1],["ivi",-1,9],["ico",-1,1],["ismo",-1,1],["oso",-1,1],["amento",-1,6],["imento",-1,6],["ivo",-1,9],["ità",-1,8],["istà",-1,1],["istè",-1,1],["istì",-1,1]];var c=[["isca",-1,1],["enda",-1,1],["ata",-1,1],["ita",-1,1],["uta",-1,1],["ava",-1,1],["eva",-1,1],["iva",-1,1],["erebbe",-1,1],["irebbe",-1,1],["isce",-1,1],["ende",-1,1],["are",-1,1],["ere",-1,1],["ire",-1,1],["asse",-1,1],["ate",-1,1],["avate",16,1],["evate",16,1],["ivate",16,1],["ete",-1,1],["erete",20,1],["irete",20,1],["ite",-1,1],["ereste",-1,1],["ireste",-1,1],["ute",-1,1],["erai",-1,1],["irai",-1,1],["isci",-1,1],["endi",-1,1],["erei",-1,1],["irei",-1,1],["assi",-1,1],["ati",-1,1],["iti",-1,1],["eresti",-1,1],["iresti",-1,1],["uti",-1,1],["avi",-1,1],["evi",-1,1],["ivi",-1,1],["isco",-1,1],["ando",-1,1],["endo",-1,1],["Yamo",-1,1],["iamo",-1,1],["avamo",-1,1],["evamo",-1,1],["ivamo",-1,1],["eremo",-1,1],["iremo",-1,1],["assimo",-1,1],["ammo",-1,1],["emmo",-1,1],["eremmo",54,1],["iremmo",54,1],["immo",-1,1],["ano",-1,1],["iscano",58,1],["avano",58,1],["evano",58,1],["ivano",58,1],["eranno",-1,1],["iranno",-1,1],["ono",-1,1],["iscono",65,1],["arono",65,1],["erono",65,1],["irono",65,1],["erebbero",-1,1],["irebbero",-1,1],["assero",-1,1],["essero",-1,1],["issero",-1,1],["ato",-1,1],["ito",-1,1],["uto",-1,1],["avo",-1,1],["evo",-1,1],["ivo",-1,1],["ar",-1,1],["ir",-1,1],["erà",-1,1],["irà",-1,1],["erò",-1,1],["irò",-1,1]];var l=[17,65,16,0,0,0,0,0,0,0,0,0,0,0,0,128,128,8,2,1];var n=[17,65,0,0,0,0,0,0,0,0,0,0,0,0,0,128,128,8,2];var f=[17];var b=0;var m=0;var k=0;function _(){var i;var a=r.cursor;while(true){var s=r.cursor;r:{r.bra=r.cursor;i=r.find_among(e);if(i==0){break r}r.ket=r.cursor;switch(i){case 1:if(!r.slice_from("à")){return false}break;case 2:if(!r.slice_from("è")){return false}break;case 3:if(!r.slice_from("ì")){return false}break;case 4:if(!r.slice_from("ò")){return false}break;case 5:if(!r.slice_from("ù")){return false}break;case 6:if(!r.slice_from("qU")){return false}break;case 7:if(r.cursor>=r.limit){break r}r.cursor++;break}continue}r.cursor=s;break}r.cursor=a;while(true){var o=r.cursor;r:{e:while(true){var u=r.cursor;i:{if(!r.in_grouping(l,97,249)){break i}r.bra=r.cursor;a:{var t=r.cursor;s:{if(!r.eq_s("u")){break s}r.ket=r.cursor;if(!r.in_grouping(l,97,249)){break s}if(!r.slice_from("U")){return false}break a}r.cursor=t;if(!r.eq_s("i")){break i}r.ket=r.cursor;if(!r.in_grouping(l,97,249)){break i}if(!r.slice_from("I")){return false}}r.cursor=u;break e}r.cursor=u;if(r.cursor>=r.limit){break r}r.cursor++}continue}r.cursor=o;break}return true}function v(){k=r.limit;m=r.limit;b=r.limit;var e=r.cursor;r:{e:{var i=r.cursor;i:{if(!r.in_grouping(l,97,249)){break i}a:{var a=r.cursor;s:{if(!r.out_grouping(l,97,249)){break s}o:while(true){u:{if(!r.in_grouping(l,97,249)){break u}break o}if(r.cursor>=r.limit){break s}r.cursor++}break a}r.cursor=a;if(!r.in_grouping(l,97,249)){break i}s:while(true){o:{if(!r.out_grouping(l,97,249)){break o}break s}if(r.cursor>=r.limit){break i}r.cursor++}}break e}r.cursor=i;if(!r.out_grouping(l,97,249)){break r}i:{var s=r.cursor;a:{if(!r.out_grouping(l,97,249)){break a}s:while(true){o:{if(!r.in_grouping(l,97,249)){break o}break s}if(r.cursor>=r.limit){break a}r.cursor++}break i}r.cursor=s;if(!r.in_grouping(l,97,249)){break r}if(r.cursor>=r.limit){break r}r.cursor++}}k=r.cursor}r.cursor=e;var o=r.cursor;r:{e:while(true){i:{if(!r.in_grouping(l,97,249)){break i}break e}if(r.cursor>=r.limit){break r}r.cursor++}e:while(true){i:{if(!r.out_grouping(l,97,249)){break i}break e}if(r.cursor>=r.limit){break r}r.cursor++}m=r.cursor;e:while(true){i:{if(!r.in_grouping(l,97,249)){break i}break e}if(r.cursor>=r.limit){break r}r.cursor++}e:while(true){i:{if(!r.out_grouping(l,97,249)){break i}break e}if(r.cursor>=r.limit){break r}r.cursor++}b=r.cursor}r.cursor=o;return true}function g(){var e;while(true){var a=r.cursor;r:{r.bra=r.cursor;e=r.find_among(i);if(e==0){break r}r.ket=r.cursor;switch(e){case 1:if(!r.slice_from("i")){return false}break;case 2:if(!r.slice_from("u")){return false}break;case 3:if(r.cursor>=r.limit){break r}r.cursor++;break}continue}r.cursor=a;break}return true}function d(){if(!(k<=r.cursor)){return false}return true}function w(){if(!(m<=r.cursor)){return false}return true}function h(){if(!(b<=r.cursor)){return false}return true}function p(){var e;r.ket=r.cursor;if(r.find_among_b(a)==0){return false}r.bra=r.cursor;e=r.find_among_b(s);if(e==0){return false}if(!d()){return false}switch(e){case 1:if(!r.slice_del()){return false}break;case 2:if(!r.slice_from("e")){return false}break}return true}function q(){var e;r.ket=r.cursor;e=r.find_among_b(t);if(e==0){return false}r.bra=r.cursor;switch(e){case 1:if(!h()){return false}if(!r.slice_del()){return false}break;case 2:if(!h()){return false}if(!r.slice_del()){return false}var i=r.limit-r.cursor;r:{r.ket=r.cursor;if(!r.eq_s_b("ic")){r.cursor=r.limit-i;break r}r.bra=r.cursor;if(!h()){r.cursor=r.limit-i;break r}if(!r.slice_del()){return false}}break;case 3:if(!h()){return false}if(!r.slice_from("log")){return false}break;case 4:if(!h()){return false}if(!r.slice_from("u")){return false}break;case 5:if(!h()){return false}if(!r.slice_from("ente")){return false}break;case 6:if(!d()){return false}if(!r.slice_del()){return false}break;case 7:if(!w()){return false}if(!r.slice_del()){return false}var a=r.limit-r.cursor;r:{r.ket=r.cursor;e=r.find_among_b(o);if(e==0){r.cursor=r.limit-a;break r}r.bra=r.cursor;if(!h()){r.cursor=r.limit-a;break r}if(!r.slice_del()){return false}switch(e){case 1:r.ket=r.cursor;if(!r.eq_s_b("at")){r.cursor=r.limit-a;break r}r.bra=r.cursor;if(!h()){r.cursor=r.limit-a;break r}if(!r.slice_del()){return false}break}}break;case 8:if(!h()){return false}if(!r.slice_del()){return false}var s=r.limit-r.cursor;r:{r.ket=r.cursor;if(r.find_among_b(u)==0){r.cursor=r.limit-s;break r}r.bra=r.cursor;if(!h()){r.cursor=r.limit-s;break r}if(!r.slice_del()){return false}}break;case 9:if(!h()){return false}if(!r.slice_del()){return false}var c=r.limit-r.cursor;r:{r.ket=r.cursor;if(!r.eq_s_b("at")){r.cursor=r.limit-c;break r}r.bra=r.cursor;if(!h()){r.cursor=r.limit-c;break r}if(!r.slice_del()){return false}r.ket=r.cursor;if(!r.eq_s_b("ic")){r.cursor=r.limit-c;break r}r.bra=r.cursor;if(!h()){r.cursor=r.limit-c;break r}if(!r.slice_del()){return false}}break}return true}function z(){if(r.cursor<k){return false}var e=r.limit_backward;r.limit_backward=k;r.ket=r.cursor;if(r.find_among_b(c)==0){r.limit_backward=e;return false}r.bra=r.cursor;if(!r.slice_del()){return false}r.limit_backward=e;return true}function I(){var e=r.limit-r.cursor;r:{r.ket=r.cursor;if(!r.in_grouping_b(n,97,242)){r.cursor=r.limit-e;break r}r.bra=r.cursor;if(!d()){r.cursor=r.limit-e;break r}if(!r.slice_del()){return false}r.ket=r.cursor;if(!r.eq_s_b("i")){r.cursor=r.limit-e;break r}r.bra=r.cursor;if(!d()){r.cursor=r.limit-e;break r}if(!r.slice_del()){return false}}var i=r.limit-r.cursor;r:{r.ket=r.cursor;if(!r.eq_s_b("h")){r.cursor=r.limit-i;break r}r.bra=r.cursor;if(!r.in_grouping_b(f,99,103)){r.cursor=r.limit-i;break r}if(!d()){r.cursor=r.limit-i;break r}if(!r.slice_del()){return false}}return true}this.stem=function(){var e=r.cursor;_();r.cursor=e;v();r.limit_backward=r.cursor;r.cursor=r.limit;var i=r.limit-r.cursor;p();r.cursor=r.limit-i;var a=r.limit-r.cursor;r:{e:{var s=r.limit-r.cursor;i:{if(!q()){break i}break e}r.cursor=r.limit-s;if(!z()){break r}}}r.cursor=r.limit-a;var o=r.limit-r.cursor;I();r.cursor=r.limit-o;r.cursor=r.limit_backward;var u=r.cursor;g();r.cursor=u;return true};this["stemWord"]=function(e){r.setCurrent(e);this.stem();return r.getCurrent()}};