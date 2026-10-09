---
title: Publications
---

<div class="pub">
<img class="pub-preview" src="/assets/img/publication_preview/dissertation.png" alt="">
<div class="pub-body">
<div class="pub-title">Bridging Probabilistic Circuits and Deep Neural Networks</div>
<div>Steven Braun</div>
<div><em>Ph.D. Thesis, Technische Universität Darmstadt</em>, 2026</div>
<div class="pub-links"><a href="https://tuprints.ulb.tu-darmstadt.de/bitstreams/1c4d661a-2870-4d27-9c2f-bfde36997754/download">PDF</a> <a href="https://tuprints.ulb.tu-darmstadt.de/handle/tuda/15123">Website</a></div>
<details><summary>Abstract</summary><p>Deep neural networks (DNNs) have achieved remarkable success in learning complex functions from data, yet they often lack the principled probabilistic reasoning and tractability of models like probabilistic circuits (PCs). This creates a fundamental dichotomy in modern machine learning, putting the expressiveness and scalability of DNNs against the inference flexibility and probabilistic benefits of PCs. This dissertation aims to bridge this divide through a two-sided research agenda: first, by advancing the capabilities of PCs through the integration of deep learning principles, and second, by leveraging probabilistic models as components within the broader deep learning ecosystem to create more robust and capable hybrid systems.</p><p>To address the limitations of PCs, we first introduce einsum networks, a tensorized framework that reformulates circuit computations to enable scalable, hardware-accelerated training, yielding orders-of-magnitude speedups. We then develop a differentiable sampling procedure that enables the use of arbitrary, sample-based training objectives, moving PCs beyond traditional maximum likelihood estimation. Finally, we propose tractable dropout inference (TDI), a novel, closed-form method to quantify epistemic uncertainty in a single forward pass, enabling PCs to reliably detect out-of-distribution data.</p><p>Building on these advancements, we shift focus from enhancing PCs to leveraging them in collaboration with DNNs. We introduce autoencoding probabilistic circuits (APCs), a hybrid architecture that pairs a tractable PC encoder with a neural decoder. By modeling the joint data-embedding distribution, APCs achieve principled representation learning and are uniquely robust to missing data through exact marginalization. Extending this approach beyond hybrid architectures, we reframe knowledge distillation from a probabilistic viewpoint, leading to contrastive abductive knowledge extraction (CAKE), a fully data-free and model-agnostic procedure for deep classifier mimicry.</p><p>Collectively, these contributions demonstrate that PCs and DNNs are not mutually exclusive paradigms but rather complementary approaches that can be combined to create more capable and robust models. This work provides a computational and conceptual contribution for developing hybrid systems that unite the representational power of deep learning with the rigorous, tractable inference of probabilistic models, paving the way for more robust, flexible, and reliable artificial intelligence.</p></details>
<details><summary>BibTeX</summary><pre>@phdthesis{braun2026dissertation,
  title    = {Bridging Probabilistic Circuits and Deep Neural Networks},
  author   = {Braun, Steven},
  year     = {2026},
  month    = {feb},
  school   = {Technische Universität Darmstadt},
  address  = {Darmstadt},
  note     = {Ph.D. Thesis, Primary publication},
  doi      = {10.26083/tuda-7775},
  url      = {https://tuprints.ulb.tu-darmstadt.de/handle/tuda/15123},
  urn      = {urn:nbn:de:tuda-tuda-151233},
  language = {English}
}</pre></details>
</div>
</div>

<div class="pub">
<img class="pub-preview" src="/assets/img/publication_preview/braun2025apc.png" alt="">
<div class="pub-body">
<div class="pub-title">Tractable Representation Learning with Probabilistic Circuits</div>
<div>Steven Braun, Sahil Sidheekh, Antonio Vergari, Martin Mundt, Sriraam Natarajan, Kristian Kersting</div>
<div><em>Transactions on Machine Learning Research</em>, 2025</div>
<div class="pub-links"><a href="https://openreview.net/pdf?id=h8D75pVKja">PDF</a> <a href="/assets/pdf/apcs-poster-tpm-2025.pdf">Poster</a></div>
<details><summary>Abstract</summary><p>Probabilistic circuits (PCs) are powerful probabilistic models that enable exact and tractable inference, making them highly suitable for probabilistic reasoning and inference tasks. While dominant in neural networks, representation learning with PCs remains underexplored, with prior approaches relying on external neural embeddings or activation-based encodings. To address this gap, we introduce autoencoding probabilistic circuits (APCs), a novel framework leveraging the tractability of PCs to model probabilistic embeddings explicitly. APCs extend PCs by jointly modeling data and embeddings, obtaining embedding representations through tractable probabilistic inference. The PC encoder allows the framework to natively handle arbitrary missing data and is seamlessly integrated with a neural decoder in a hybrid, end-to-end trainable architecture enabled by differentiable sampling. Our empirical evaluation demonstrates that APCs outperform existing PC-based autoencoding methods in reconstruction quality, generate embeddings competitive with, and exhibit superior robustness in handling missing data compared to neural autoencoders. These results highlight APCs as a powerful and flexible representation learning method that exploits the probabilistic inference capabilities of PCs, showing promising directions for robust inference, out-of-distribution detection, and knowledge distillation.</p></details>
<details><summary>BibTeX</summary><pre>@article{braun2025apcs,
  title   = {Tractable Representation Learning with Probabilistic Circuits},
  author  = {Steven Braun and Sahil Sidheekh and Antonio Vergari and Martin Mundt and Sriraam Natarajan and Kristian Kersting},
  year    = {2025},
  journal = {Transactions on Machine Learning Research}
}</pre></details>
</div>
</div>

<div class="pub">
<img class="pub-preview" src="/assets/img/publication_preview/braun2023cake.png" alt="">
<div class="pub-body">
<div class="pub-title">Deep Classifier Mimicry without Data Access</div>
<div>Steven Braun, Martin Mundt, Kristian Kersting</div>
<div><em>International Conference on Artificial Intelligence and Statistics (AISTATS) – Oral &amp; Student Paper Highlight Award</em>, 2024</div>
<div class="pub-links"><a href="https://proceedings.mlr.press/v238/braun24b/braun24b.pdf">PDF</a> <a href="/assets/pdf/cake-poster-aistats-2024.pdf">Poster</a> <a href="/assets/pdf/cake-oral-aistats-2024.pdf">Slides</a></div>
<details><summary>Abstract</summary><p>Access to pre-trained models has recently emerged as a standard across numerous machine learning domains. Unfortunately, access to the original data the models were trained on may not equally be granted. This makes it tremendously challenging to fine-tune, compress models, adapt continually, or to do any other type of data-driven update. We posit that original data access may however not be required. Specifically, we propose Contrastive Abductive Knowledge Extraction (CAKE), a model-agnostic knowledge distillation procedure that mimics deep classifiers without access to the original data. To this end, CAKE generates pairs of noisy synthetic samples and diffuses them contrastively toward a model&#x27;s decision boundary. We empirically corroborate CAKE&#x27;s effectiveness using several benchmark datasets and various architectural choices, paving the way for broad application.</p></details>
<details><summary>BibTeX</summary><pre>@article{braun2023cake,
  title   = {Deep Classifier Mimicry without Data Access},
  author  = {Steven Braun and Martin Mundt and Kristian Kersting},
  year    = {2024},
  journal = {International Conference on Artificial Intelligence and Statistics (AISTATS) -- Oral &amp; Student Paper Highlight Award}
}</pre></details>
</div>
</div>

<div class="pub">
<img class="pub-preview" src="/assets/img/publication_preview/braun2023tdi.png" alt="">
<div class="pub-body">
<div class="pub-title">Probabilistic Circuits That Know What They Don't Know</div>
<div>Fabrizio Ventola*, Steven Braun*, Zhongjie Yu, Martin Mundt, Kristian Kersting</div>
<div><em>Proceedings of the 39th Conference on Uncertainty in Artificial Intelligence (UAI)</em>, 2023</div>
<div class="pub-links"><a href="https://proceedings.mlr.press/v216/ventola23a/ventola23a.pdf">PDF</a> <a href="https://proceedings.mlr.press/v216/ventola23a/ventola23a-supp.pdf">Supp</a> <a href="https://github.com/ml-research/tractable-dropout-inference">Code</a> <a href="/assets/pdf/tdi-poster-uai-2023.pdf">Poster</a> <a href="/assets/pdf/tdi-oral-uai-2023.pdf">Slides</a> <a href="https://www.youtube.com/watch?v=B9xiDeYgu7Q">Video</a></div>
<details><summary>Abstract</summary><p>Probabilistic circuits (PCs) are models that allow exact
                  and tractable probabilistic inference. In contrast to neural
                  networks, they are often assumed to be well-calibrated and
                  robust to out-of-distribution (OOD) data. In this paper, we
                  show that PCs are in fact not robust to OOD data, i.e., they
                  don&#x27;t know what they don&#x27;t know. We then show how this
                  challenge can be overcome by model uncertainty quantification.
                  To this end, we propose tractable dropout inference (TDI), an
                  inference procedure to estimate uncertainty by deriving an
                  analytical solution to Monte Carlo dropout (MCD) through
                  variance propagation. Unlike MCD in neural networks, which
                  comes at the cost of multiple network evaluations, TDI
                  provides tractable sampling-free uncertainty estimates in a
                  single forward pass. TDI improves the robustness of PCs to
                  distribution shift and OOD data, demonstrated through a series
                  of experiments evaluating the classification confidence and
                  uncertainty estimates on real-world data.</p></details>
<details><summary>BibTeX</summary><pre>@article{braun2023tdi,
  author  = {Ventola*, Fabrizio and Braun*, Steven and Yu, Zhongjie and Mundt, Martin and Kersting, Kristian},
  title   = {Probabilistic Circuits That Know What They Don&#x27;t Know},
  year    = {2023},
  journal = {Proceedings of the 39th Conference on Uncertainty in Artificial Intelligence (UAI)}
}</pre></details>
</div>
</div>

<div class="pub">
<img class="pub-preview" src="/assets/img/publication_preview/trapp2022towards.png" alt="">
<div class="pub-body">
<div class="pub-title">Towards Coreset Learning in Probabilistic Circuits</div>
<div>Martin Trapp, Steven Lang, Aastha Shah, Martin Mundt, Kristian Kersting, Arno Solin</div>
<div><em>The 5th Workshop on Tractable Probabilistic Modeling (UAI)</em>, 2022</div>
<div class="pub-links"><a href="https://openreview.net/pdf?id=bt2cS60SxSP">PDF</a></div>
<details><summary>Abstract</summary><p>Probabilistic circuits (PCs) are a powerful family of
                  tractable probabilistic models, guaranteeing efficient and
                  exact computation of many probabilistic inference queries.
                  However, their sparsely structured nature makes computations
                  on large data sets challenging to perform. Recent works have
                  focused on tensorized representations of PCs to speed up
                  computations on large data sets. In this work, we present an
                  orthogonal approach by sparsifying the set of $n$ observations
                  and show that finding a coreset of $k\ll n$ data points can be
                  phrased as a monotone submodular optimisation problem which
                  can be solved greedily for a deterministic PCs of $|\G|$ nodes
                  in $\mathcal{O}(k \, n \, |\G|)$. Finally, we verify on a
                  series of data sets that our greedy algorithm outperforms
                  random selection.</p></details>
<details><summary>BibTeX</summary><pre>@inproceedings{trapp2022towards,
  title     = {Towards Coreset Learning in Probabilistic Circuits},
  author    = {Martin Trapp and Steven Lang and Aastha Shah and Martin Mundt and Kristian Kersting and Arno Solin},
  booktitle = {The 5th Workshop on Tractable Probabilistic Modeling (UAI)},
  year      = {2022}
}</pre></details>
</div>
</div>

<div class="pub">
<img class="pub-preview" src="/assets/img/publication_preview/mundt2021clevacompass.png" alt="">
<div class="pub-body">
<div class="pub-title">CLEVA-Compass: A Continual Learning EValuation Assessment Compass to Promote Research Transparency and Comparability</div>
<div>Martin Mundt, Steven Lang, Quentin Delfosse, Kristian Kersting</div>
<div><em>International Conference on Learning Representations (ICLR)</em>, 2022</div>
<div class="pub-links"><a href="https://openreview.net/pdf?id=rHMaBYbkkRJ">PDF</a> <a href="https://github.com/ml-research/CLEVA-Compass">Code</a></div>
<details><summary>Abstract</summary><p>What is the state of the art in continual machine learning?
                  Although a natural question for predominant static benchmarks,
                  the notion to train systems in a life- long manner entails a
                  plethora of additional challenges with respect to set-up and
                  evaluation. The latter have recently sparked a growing amount
                  of critiques on prominent algorithm-centric perspectives and
                  evaluation protocols being too nar- row, resulting in several
                  attempts at constructing guidelines in favor of specific
                  desiderata or arguing against the validity of prevalent
                  assumptions. In this work, we depart from this mindset and
                  argue that the goal of a precise formulation of desiderata is
                  an ill-posed one, as diverse applications may always warrant
                  distinct scenarios. Instead, we introduce the Continual
                  Learning EValuation Assessment Compass: the CLEVA-Compass. The
                  compass provides the visual means to both identify how
                  approaches are practically reported and how works can
                  simultane- ously be contextualized in the broader literature
                  landscape. In addition to promot- ing compact specification in
                  the spirit of recent replication trends, it thus provides an
                  intuitive chart to understand the priorities of individual
                  systems, where they resemble each other, and what elements are
                  missing towards a fair comparison.</p></details>
<details><summary>BibTeX</summary><pre>@inproceedings{mundt2021clevacompass,
  title     = {CLEVA-Compass: A Continual Learning EValuation Assessment Compass to Promote Research Transparency and Comparability},
  author    = {Martin Mundt and Steven Lang and Quentin Delfosse and Kristian Kersting},
  year      = {2022},
  booktitle = {International Conference on Learning Representations (ICLR)}
}</pre></details>
</div>
</div>

<div class="pub">
<img class="pub-preview" src="/assets/img/publication_preview/lang2022diff-sampling-spns.jpg" alt="">
<div class="pub-body">
<div class="pub-title">Elevating Perceptual Sample Quality in Probabilistic Circuits through Differentiable Sampling</div>
<div>Steven Lang, Martin Mundt, Fabrizio Ventola, Robert Peharz, Kristian Kersting</div>
<div><em>Proceedings of Machine Learning Research, Workshop on Preregistration in Machine Learning (NeurIPS)</em>, 2022</div>
<div class="pub-links"><a href="https://proceedings.mlr.press/v181/lang22a/lang22a.pdf">PDF</a> <a href="https://preregister.science/posters_21neurips/10_poster.png">Poster</a> <a href="https://youtu.be/8aTnMHtTIRc">Slides</a></div>
<details><summary>Abstract</summary><p>Deep generative models have seen a dramatic improvement in
                  recent years, due to the use of alternative losses based on
                  perceptual assessment of generated samples. This improvement
                  has not yet been applied to the model class of probabilistic
                  circuits (PCs), presumably due to significant technical
                  challenges concerning differentiable sampling, which is a key
                  requirement for optimizing perceptual losses. This is
                  unfortunate, since PCs allow a much wider range of
                  probabilistic inference routines than main-stream generative
                  models, such as exact and efficient marginalization and
                  conditioning. Motivated by the success of loss reframing in
                  deep generative models, we incorporate perceptual metrics into
                  the PC learning objective. To this aim, we introduce a
                  differentiable sampling procedure for PCs, where the central
                  challenge is the non-differentiability of sampling from the
                  categorical distribution over latent PC variables. We take
                  advantage of the Gumbel-Softmax trick and develop a novel
                  inference pass to smoothly interpolate child samples as a
                  strategy to circumvent non-differentiability of sum node
                  sampling. We initially hypothesized, that perceptual losses,
                  unlocked by our novel differentiable sampling procedure, will
                  elevate the generative power of PCs and improve their sample
                  quality to be on par with neural counterparts like
                  probabilistic auto-encoders and generative adversarial
                  networks. Although our experimental findings empirically
                  reject this hypothesis for now, the results demonstrate that
                  samples drawn from PCs optimized with perceptual losses can
                  have similar sample quality compared to likelihood-based
                  optimized PCs and, at the same time, can express richer
                  contrast, colors, and details. Whereas before, PCs were
                  restricted to likelihood-based optimization, this work has
                  paved the way to advance PCs with loss formulations that have
                  been built around deep neural networks in recent years.</p></details>
<details><summary>BibTeX</summary><pre>@inproceedings{lang2022diff-sampling-spns,
  title     = {Elevating Perceptual Sample Quality in Probabilistic Circuits through Differentiable Sampling},
  author    = {Steven Lang and Martin Mundt and Fabrizio Ventola and Robert Peharz and Kristian Kersting},
  booktitle = {Proceedings of Machine Learning Research, Workshop on Preregistration in Machine Learning (NeurIPS)},
  year      = {2022},
  volume    = {181},
  series    = {Proceedings of Machine Learning Research},
  pages     = {1--25},
  publisher = {PMLR}
}</pre></details>
</div>
</div>

<div class="pub">
<img class="pub-preview" src="/assets/img/publication_preview/lang2021dafne.jpg" alt="">
<div class="pub-body">
<div class="pub-title">DAFNe: A One-Stage Anchor-Free Deep Model for Oriented Object Detection</div>
<div>Steven Lang, Fabrizio Ventola, Kristian Kersting</div>
<div><em>arXiv preprint, arXiv:2109.06148</em>, 2021</div>
<div class="pub-links"><a href="https://github.com/braun-steven/DAFNe">Code</a> <a href="https://arxiv.org/abs/2109.06148">arXiv</a></div>
<details><summary>Abstract</summary><p>We present DAFNe, a Dense one-stage Anchor-Free deep
                  Network for oriented object detection. As a one-stage model,
                  it performs bounding box predictions on a dense grid over the
                  input image, being architecturally simpler in design, as well
                  as easier to optimize than its two-stage counterparts.
                  Furthermore, as an anchor-free model, it reduces the
                  prediction complexity by refraining from employing bounding
                  box anchors. With DAFNe we introduce an orientation-aware
                  generalization of the center-ness function for arbitrarily
                  oriented bounding boxes to down-weight low-quality predictions
                  and a center-to-corner bounding box prediction strategy that
                  improves object localization performance. Our experiments show
                  that DAFNe outperforms all previous one-stage anchor-free
                  models on DOTA 1.0, DOTA 1.5, and UCAS-AOD and is on par with
                  the best models on HRSC2016.</p></details>
<details><summary>BibTeX</summary><pre>@article{lang2021dafne,
  title         = {DAFNe: A One-Stage Anchor-Free Deep Model for Oriented Object Detection},
  author        = {Steven Lang and Fabrizio Ventola and Kristian Kersting},
  year          = {2021},
  eprint        = {2109.06148},
  archiveprefix = {arXiv},
  primaryclass  = {cs.CV},
  journal       = {arXiv preprint, arXiv:2109.06148}
}</pre></details>
</div>
</div>

<div class="pub">
<img class="pub-preview" src="/assets/img/publication_preview/pmlr-v119-peharz20a.png" alt="">
<div class="pub-body">
<div class="pub-title">Einsum Networks: Fast and Scalable Learning of Tractable Probabilistic Circuits</div>
<div>Robert Peharz, Steven Lang, Antonio Vergari, Karl Stelzner, Alejandro Molina, Martin Trapp, Guy Van Den Broeck, Kristian Kersting, Zoubin Ghahramani</div>
<div><em>Proceedings of the 37th International Conference on Machine Learning (ICML)</em>, 2020</div>
<div class="pub-links"><a href="http://proceedings.mlr.press/v119/peharz20a/peharz20a.pdf">PDF</a> <a href="https://github.com/cambridge-mlg/EinsumNetworks">Code</a></div>
<details><summary>Abstract</summary><p>Probabilistic circuits (PCs) are a promising av- enue for
                  probabilistic modeling, as they permit a wide range of exact
                  and efficient inference rou- tines. Recent
                  “deep-learning-style” implementa- tions of PCs strive for a
                  better scalability, but are still difficult to train on
                  real-world data, due to their sparsely connected computational
                  graphs. In this paper, we propose Einsum Networks (EiNets), a
                  novel implementation design for PCs, improving prior art in
                  several regards. At their core, EiNets combine a large number
                  of arithmetic operations in a single monolithic
                  einsum-operation, leading to speedups and memory savings of up
                  to two orders of magnitude, in comparison to previous
                  implementations. As an algorithmic contribution, we show that
                  the implementation of Expectation- Maximization (EM) can be
                  simplified for PCs, by leveraging automatic differentiation.
                  Further- more, we demonstrate that EiNets scale well to
                  datasets which were previously out of reach, such as SVHN and
                  CelebA, and that they can be used as faithful generative image
                  models.</p></details>
<details><summary>BibTeX</summary><pre>@inproceedings{pmlr-v119-peharz20a,
  title     = {Einsum Networks: Fast and Scalable Learning of Tractable Probabilistic Circuits},
  author    = {Peharz, Robert and Lang, Steven and Vergari, Antonio and Stelzner, Karl and Molina, Alejandro and Trapp, Martin and Van Den Broeck, Guy and Kersting, Kristian and Ghahramani, Zoubin},
  booktitle = {Proceedings of the 37th International Conference on Machine Learning (ICML)},
  pages     = {7563--7574},
  year      = {2020},
  editor    = {Hal Daumé III and Aarti Singh},
  volume    = {119},
  series    = {Proceedings of Machine Learning Research},
  publisher = {PMLR},
  url       = {http://proceedings.mlr.press/v119/peharz20a.html}
}</pre></details>
</div>
</div>

<div class="pub">
<img class="pub-preview" src="/assets/img/publication_preview/lang2019wekadeeplearning4j.jpg" alt="">
<div class="pub-body">
<div class="pub-title">WekaDeeplearning4j: A deep learning package for Weka based on Deeplearning4j</div>
<div>Steven Lang, Felipe Bravo-Marquez, Christopher Beckham, Mark Hall, Eibe Frank</div>
<div><em>Knowledge-Based Systems</em>, 2019</div>
<div class="pub-links"><a href="/assets/pdf/WDL4J_KBS2019.pdf">PDF</a> <a href="https://github.com/Waikato/wekaDeeplearning4j">Code</a></div>
<details><summary>Abstract</summary><p>Deep learning is a branch of machine learning that
                  generates multi-layered representations of data, commonly
                  using artificial neural networks, and has improved the
                  state-of-the-art in various machine learning tasks (e.g.,
                  image classification, object detection, speech recognition,
                  and document classifica- tion). However, most popular deep
                  learning frameworks such as TensorFlow and PyTorch require
                  users to write code to apply deep learning. We present
                  WekaDeeplearning4j, a Weka package that makes deep learning
                  accessible through a graphical user interface (GUI). The
                  package uses Deeplearning4j as its backend, provides GPU
                  support, and enables GUI-based training of deep neural
                  networks such as convolutional and recurrent neural networks.
                  It also provides pre-processing functionality for image and
                  text data.</p></details>
<details><summary>BibTeX</summary><pre>@article{lang2019wekadeeplearning4j,
  title     = {WekaDeeplearning4j: A deep learning package for Weka based on Deeplearning4j},
  author    = {Lang, Steven and Bravo-Marquez, Felipe and Beckham, Christopher and Hall, Mark and Frank, Eibe},
  journal   = {Knowledge-Based Systems},
  volume    = {178},
  pages     = {48 - 50},
  year      = {2019},
  issn      = {0950-7051},
  doi       = {https://doi.org/10.1016/j.knosys.2019.04.013},
  url       = {http://www.sciencedirect.com/science/article/pii/S0950705119301789},
  publisher = {Elsevier}
}</pre></details>
</div>
</div>

\* denotes equal contribution. [Download all as BibTeX](/assets/bibliography/papers.bib) · [Google Scholar](https://scholar.google.com/citations?user=sja9tq0AAAAJ)
