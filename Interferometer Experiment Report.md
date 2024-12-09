
<h1> <p style="font-size:24px">Mach-Zender Interferometer Experiment Report </h1>
<p style="font-size:12px">Keisha Valenzuela and Javier Bates</p><br><p style="font-size:9px">valenzuela.keisha07@gmail.com</p>
<p style="font-size:30px">Introduction</p></h1>

The purpose of this experiment was to investiage how varying beam path length and horizontal alignment affect interference patterns produced by a Michelson interfermoeter using a Helium-Neon (HeNe) laser.

Interferometry is a technique for measuring wave interference based on the principle of superposition. This principle states that when two or more waves overlap at a point, their resulting displacement is the sum of their individual displacements at that point (Bryan & Hellemans, 2004, p. 695). By using electromagnetic waves, interferometers generate and analyze interference patterns, which arise from constructive interference (where wave peaks align) and destructive interference (where peaks and troughs cancel each other out). These patterns are key to making precise measurements in optical experiments that ustlise this technique.

In order to construct and effective interferometer, one requires an understanding of one of the fundamental properiteis of light, specifically refraction. Refraction dictates how light interacts with reflective surfaces, such as mirrors. The law of reflection states that the angle of incidence (the angle at which a ray of light strikes a reflective surface) is equal to the angle of reflection (the angle at which it bounces off). This principle ensures the precise alignment of mirrors, which is crucial for producing clear and reliable interference patterns (Wood, 2024).

![Law of refelction](<Images/Images for Report/Law of reflection diagram.png>)

<small> _Figure 1. Visual of the law of reflection_

<big>
Additionally, Interferometers rely on the superposition principal and nature of light waves to produce interference fringes visualised as dark spaces in projected light. The experiment relies on the symmetry of all elements; If the two beams intensity are unequal, the conclusion you draw from changing variables would be unreliable due to the absence of a base measurement. In this experiment the ‘base measurement’ would be when the beams align at all peaks, showing equal fringes. This cannot happen if the beams are different intensities as the beams do not equally contribute to the peaks.

In this experiment we explored the impact of beam length and horizontal shift on the interference pattern.

After constructing the interferometer, the power measured of the final interference beam had major fluctuations between 0.3 and 0.7 micro watts. To determine the major contributing factors to the fluctuation a Fast Fourier Transform (FFT) was applied to the recorded data.

### <p style="font-size:30px">Materials and Methods</p>

### <p style="font-size:30p">materials</p>

### <p style="font-size:30px">Setup construction</p>

![Interferometer diagram](<Images/Images for Report/Mach-Zender Interferometer Diagram Correct.png>)
<small> _Figure 2. Mach-Zender Beam splitter diagram slightly modified from: (ChaosFlaws, 2016)_

<big> The first step was to tighten the bases of all elements to match the same height as the laser placing the optical elements before the laser and center the beam roughly in the center of the element.

The approximate location of the first mirror of arm one was identified. This position was marked and the translation stage was screwed into the table using the marked area as a guide. The first mirror was screwed into the right of the translation stage, and it was rotated slightly left. To track the beams movement a white card was held up and moved alongside the mirror. After reaching an approximate right angle the second mirror was placed in the beams path. This was a challenge due to the translation stage not being wide enough to accommodate both the mirrors’ bases. This was fixed by increasing the angle that the first mirror faced at to take up less horizontal space (_adjustments seen on figure 4_).

To ensure simplicity in construction, an initial position was chosen for the second beam-splitter. The third mirror of arm one was positioned along the same row as the second beam-splitter as symmetry is crucial to the success of the interferometer. To construct the second arm a mirror was fastened at the intersection of the two beam-splitters, no adjustments was done to the angle of the mirror at this time.

![Mirror diagram](<Images/Images for Report/mirror diagram pptx.jpg>)
<Small> _Figure 3. Diagram of a Thorlabs mirror, denoting its adjusters._
<big>

The horizontal shift knob was used to rotate the mirror, changing the angle of reflection as mentioned in the introduction to bounce into the beam-splitter.All the mirrors were adjusted until the output beam was a single dot seen _figure 4_. To be as accurate as possible, one arm was continuously blocked and unblocked to spot if there was any movement from one beam to the next.This process was repeated until there was no visual shift to the dot when each beam was blocked individually.

![Beam path](<Images/Images for Report/Beam path.png>)
<small> _figure 4. Visualised beam path of the laser_

### <p style="font-size:20px">Challenges and adjustments</p>



When adjusting the mirrors to form a single output, it was found that, though visually one dot, the fringes did not cover the entire dot. This indicated that the vertical alignment of the beams was off. To fix this problem the vertical shift knobs seen in _figure 3_ were adjusted until the mirror was perpendicular to the table.

### <p style="font-size:30px">Results and Observations</p>


### <p style="font-size:30px">Sources of interferance</p>

Sources of Fluctuation

o Environmental vibrations
o Thermal effects
o Imperfect alignment

# References

Bryan, B., & Hellemans, A. (2004). The history of science and technology. New York: Scientific Publishing Inc.

ChaosFlaws. (2016). Outcome of Mach-Zehnder interferometer experiment. Retrieved from https://physics.stackexchange.com/questions/274379/outcome-of-mach-zehnder-interferometer-experiment

CUEMATH. (2023). Percent Difference. Retrieved from https://www.cuemath.com/commercial-math/percent-difference/

Wood, D. (2024). Reflection: Angle of Incidence, Curved Surfaces & Diffusion. Retrieved from https://study.com/academy/lesson/reflection-angle-of-incidence-curved-surfaces-diffusion.html#:~:text=The%20law%20of%20reflection%20says,surface%20(angle%20of%20reflection)

# Appendices

### <p style="font-size:20px">Appendix 1</p> <p style="font-size:13px">(CUEMATH, 2023)</p>

<ins>% difference= $\frac{difference}{Average}\times100$ </ins>

### Without ND filters

Difference without ND filters
= $0.373-0.327= 0.046$

Average without ND filters
= $\frac{(0.373 + 0.327)}{2}\times100 = \frac{0.7}{2}\,100 = 35$

% Diff without ND filters = $\frac{0.046}{35}\times100=$**<ins> 0.1 </ins>** (1.s.f)

### With ND filters

Difference with ND filters = $0.331-0.327= 0.004$

Average with ND filters = $\frac{(0.331+0.327)}{2}\times100 = 0.329 \times 100 = 32.9$

% diff without ND filters= $\frac{0.004}{32.9}\times100$ = **<ins>0.0001</ins>** (1.s.f)
