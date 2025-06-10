0:	addi   x1  , x0  , 16
4:	slli   x1  , x1  , 8
8:	addi   x2  , x0  , 0
12:	addi   x3  , x0  , 5
16:	beq    x2  , x3  , 56
20:	addi   x4  , x0  , 17
24:	slli   x4  , x4  , 8
28:	ori    x4  , x4  , 17
32:	slli   x4  , x4  , 8
36:	ori    x4  , x4  , 17
40:	slli   x4  , x4  , 8
44:	ori    x4  , x4  , 17
48:	add    x4  , x4  , x2
52:	slli   x5  , x2  , 2
56:	add    x6  , x1  , x5
60:	sw     x4  , 0(x6)
64:	addi   x2  , x2  , 1
68:	jal    x0  , -56
72:	addi   x2  , x0  , 0
76:	addi   x7  , x0  , 0
80:	addi   x3  , x0  , 5
84:	beq    x2  , x3  , 60
88:	slli   x5  , x2  , 2
92:	add    x6  , x1  , x5
96:	lw     x8  , 0(x6)
100:	lh     x9  , 0(x6)
104:	lhu    x10 , 0(x6)
108:	lb     x11 , 0(x6)
112:	lbu    x12 , 0(x6)
116:	add    x7  , x7  , x8
120:	xor    x7  , x7  , x9
124:	or     x7  , x7  , x10
128:	and    x7  , x7  , x11
132:	add    x7  , x7  , x12
136:	addi   x2  , x2  , 1
140:	jal    x0  , -60
144:	addi   x1  , x0  , 20
148:	slli   x1  , x1  , 8
152:	addi   x2  , x0  , 0
156:	addi   x3  , x0  , 5
160:	beq    x2  , x3  , 56
164:	addi   x4  , x0  , 34
168:	slli   x4  , x4  , 8
172:	ori    x4  , x4  , 34
176:	slli   x4  , x4  , 8
180:	ori    x4  , x4  , 34
184:	slli   x4  , x4  , 8
188:	ori    x4  , x4  , 34
192:	add    x4  , x4  , x2
196:	slli   x5  , x2  , 2
200:	add    x6  , x1  , x5
204:	sw     x4  , 0(x6)
208:	addi   x2  , x2  , 1
212:	jal    x0  , -56
216:	addi   x2  , x0  , 0
220:	addi   x3  , x0  , 5
224:	beq    x2  , x3  , 40
228:	slli   x5  , x2  , 2
232:	add    x6  , x1  , x5
236:	lw     x8  , 0(x6)
240:	lh     x9  , 0(x6)
244:	lhu    x10 , 0(x6)
248:	lb     x11 , 0(x6)
252:	lbu    x12 , 0(x6)
256:	addi   x2  , x2  , 1
260:	jal    x0  , -40
264:	addi   x1  , x0  , 24
268:	slli   x1  , x1  , 8
272:	addi   x2  , x0  , 0
276:	addi   x3  , x0  , 5
280:	beq    x2  , x3  , 56
284:	addi   x4  , x0  , 51
288:	slli   x4  , x4  , 8
292:	ori    x4  , x4  , 51
296:	slli   x4  , x4  , 8
300:	ori    x4  , x4  , 51
304:	slli   x4  , x4  , 8
308:	ori    x4  , x4  , 51
312:	add    x4  , x4  , x2
316:	slli   x5  , x2  , 2
320:	add    x6  , x1  , x5
324:	sw     x4  , 0(x6)
328:	addi   x2  , x2  , 1
332:	jal    x0  , -56
336:	addi   x2  , x0  , 0
340:	addi   x3  , x0  , 5
344:	beq    x2  , x3  , 40
348:	slli   x5  , x2  , 2
352:	add    x6  , x1  , x5
356:	lw     x8  , 0(x6)
360:	lh     x9  , 0(x6)
364:	lhu    x10 , 0(x6)
368:	lb     x11 , 0(x6)
372:	lbu    x12 , 0(x6)
376:	addi   x2  , x2  , 1
380:	jal    x0  , -40
384:	addi   x1  , x0  , 28
388:	slli   x1  , x1  , 8
392:	addi   x2  , x0  , 0
396:	addi   x3  , x0  , 5
400:	beq    x2  , x3  , 56
404:	addi   x4  , x0  , 68
408:	slli   x4  , x4  , 8
412:	ori    x4  , x4  , 68
416:	slli   x4  , x4  , 8
420:	ori    x4  , x4  , 68
424:	slli   x4  , x4  , 8
428:	ori    x4  , x4  , 68
432:	add    x4  , x4  , x2
436:	slli   x5  , x2  , 2
440:	add    x6  , x1  , x5
444:	sw     x4  , 0(x6)
448:	addi   x2  , x2  , 1
452:	jal    x0  , -56
456:	addi   x2  , x0  , 0
460:	addi   x3  , x0  , 5
464:	beq    x2  , x3  , 40
468:	slli   x5  , x2  , 2
472:	add    x6  , x1  , x5
476:	lw     x8  , 0(x6)
480:	lh     x9  , 0(x6)
484:	lhu    x10 , 0(x6)
488:	lb     x11 , 0(x6)
492:	lbu    x12 , 0(x6)
496:	addi   x2  , x2  , 1
500:	jal    x0  , -40
504:	addi   x1  , x0  , 32
508:	slli   x1  , x1  , 8
512:	addi   x1  , x1  , 20
516:	addi   x2  , x0  , 0
520:	addi   x3  , x0  , 5
524:	beq    x2  , x3  , 56
528:	addi   x4  , x0  , 85
532:	slli   x4  , x4  , 8
536:	ori    x4  , x4  , 85
540:	slli   x4  , x4  , 8
544:	ori    x4  , x4  , 85
548:	slli   x4  , x4  , 8
552:	ori    x4  , x4  , 85
556:	add    x4  , x4  , x2
560:	slli   x5  , x2  , 2
564:	add    x6  , x1  , x5
568:	sw     x4  , 0(x6)
572:	addi   x2  , x2  , 1
576:	jal    x0  , -56
580:	addi   x20 , x0  , 18
584:	slli   x20 , x20 , 8
588:	addi   x20 , x20 , 52
592:	slli   x20 , x20 , 8
596:	addi   x20 , x20 , 86
600:	slli   x20 , x20 , 8
604:	addi   x20 , x20 , 120
608:	sw     x20 , 20(x1)
612:	sh     x20 , 26(x1)
616:	sb     x20 , 29(x1)
620:	lw     x26 , 20(x1)
624:	lh     x27 , 26(x1)
628:	lb     x28 , 29(x1)
632:	lh     x21 , 30(x1)
636:	lhu    x22 , 26(x1)
640:	lb     x23 , 27(x1)
644:	lbu    x24 , 21(x1)
648:	lw     x25 , 20(x1)
652:	addi   x1  , x0  , 32
656:	slli   x1  , x1  , 8
660:	lw     x26 , 0(x1)
664:	lw     x27 , 4(x1)
668:	lw     x28 , 8(x1)
672:	lw     x29 , 12(x1)
676:	lw     x30 , 16(x1)
