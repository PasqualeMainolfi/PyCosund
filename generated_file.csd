<CsoundSynthesizer>
<CsOptions>
-o dac
</CsOptions>
<CsInstruments>

sr	=	44100
ksmps	=	1
nchnls	=	2
0dbfs	=	1


instr 1
a1 = poscil(p4 * expseg:k(.001, .01, 1, p3 - .01, .001), p5)
outs(a1, a1)
endin

instr 2
a1 = poscil(p4 * expseg:k(.001, .01, 1, p3 - .01, .001), p5 + poscil(expseg:k(.001, .01, 1, p3 - .01, .001) * p4 * p5 + 10, p5 + 10))
outs(a1, a1)
endin

instr 3
a1 = poscil(p4 * expseg:k(.001, .01, 1, p3 - .01, .001), p5 + poscil(expseg:k(.001, .01, 1, p3 - .01, .001) * p4 * p5 + 10, p5 + 10))
outs(a1, a1)
endin



</CsInstruments>
<CsScore>
f 1	0	4096	10	1
f 2	0	100	-2	0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	21	22	23	24	25	26	27	28	29	30	31	32	33	34	35	36	37	38	39	40	41	42	43	44	45	46	47	48	49	50	51	52	53	54	55	56	57	58	59	60	61	62	63	64	65	66	67	68	69	70	71	72	73	74	75	76	77	78	79	80	81	82	83	84	85	86	87	88	89	90	91	92	93	94	95	96	97	98	99
t 0	240
i 1	2.5123827971500696	3.8094104487914637	0.5	110
i 1	2.7769153204824373	0.12082156404146338	0.5	220
i 1	3.350192276553371	1.1456652528135765	0.5	330
i 1	4.708684776687052	0.9801576633070264	0.5	440
i 1	4.883555474907825	2.7214348963713086	0.5	550
i 1	5.828532969942153	1.2875625081174602	0.5	660
i 1	5.902071584385583	0.012678228557332916	0.5	770
i 1	6.337880935638892	0.9905311061380123	0.5	880
i 1	9.238405469136426	2.0905864564502097	0.5	990
i 1	10.095593427006351	2.4700631044921724	0.5	1100
i 2	4.2782018225157605	0.013495441359326676	0.5	90
i 2	7.5901986370200065	0.22651437344780223	0.5	180
i 2	10.873296171982116	0.9358051404767649	0.5	270
i 2	16.813179873510514	0.043594683832962056	0.5	360
i 2	21.949072742958318	0.1917456080961194	0.5	450
i 2	27.158404640811384	0.40508820214891716	0.5	540
i 2	30.472539696694643	0.8135034810619151	0.5	630
i 2	35.90849643621907	0.19700982068806716	0.5	720
i 2	39.98197042459311	0.2503432173950191	0.5	810
i 2	42.013454193376944	0.22882217979103447	0.5	900
i 2	46.74883378417911	0.5981176967537285	0.5	990
i 2	51.76480590645603	0.9984179016754651	0.5	1080
i 2	56.532378064859564	0.40472350908573074	0.5	1170
i 2	59.88241103061891	0.16797001900180342	0.5	1260
i 2	63.03218876889848	0.7887371445897033	0.5	1350
i 3	0.6038286516401059	0.5398701640956654	0.5	69
i 3	3.7030919125629698	2.296471020119269	0.5	138
i 3	13.569497754962727	2.463692023773849	0.5	207
i 3	14.509939498888587	0.5512168233316347	0.5	276
i 3	22.893439166639673	0.3316182663164119	0.5	345
i 3	31.754117812573973	1.0910964024982446	0.5	414
i 3	33.84433109255969	2.8950203231676905	0.5	483
</CsScore>
</CsoundSynthesizer>