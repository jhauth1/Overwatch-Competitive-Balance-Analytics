# Overwatch Competitive Balance Analytics

A Power BI analytics project exploring hero dominance, balance volatility, and skill-scaling behavior across competitive ranks and seasons in Overwatch.

This project was designed as an exploratory analytics exercise focused on:

* metric engineering
* statistical normalization
* interactive visualization design
* competitive balance analysis

The dashboard evaluates hero performance through a series of custom standardized indices built from publicly available Overwatch statistics.

---

# Dashboard Overview

The report includes several analytical views designed to evaluate hero behavior from multiple perspectives:

## Executive Meta Overview

Analyzes:

* hero dominance
* balance volatility
* seasonal meta trends
* meta stability quadrants

## Skill Analysis

Explores:

* skill floor vs skill ceiling relationships
* mastery scaling
* accessibility vs optimization payoff
* skill variance between player tiers

## Rank-Based Behavior Analysis

Examines:

* win-rate scaling by rank
* rank sensitivity
* player skill dependency
* hero performance consistency

## Hero Deep Dive

Provides:

* hero archetype classification
* seasonal metric trends
* rank-based performance curves
* role-specific hero profiling

## Hero Balance Matrix

Compares all heroes across:

* dominance
* volatility
* mastery scaling
* skill accessibility
* meta stability

## Methodology & Metric Definitions

Documents:

* index construction
* z-score normalization
* analytical methodology
* caveats and limitations

---

# Custom Metrics

## Hero Dominance Index (HDI)

A composite measure of:

* pick rate
* win rate
* high-rank representation

Used to estimate overall meta influence and competitive importance.

---

## Balance Volatility Index (BVI)

Measures seasonal instability using:

* win-rate variability
* pick-rate variability

Higher values indicate stronger patch sensitivity and balance fluctuations.

---

## Skill Ceiling Index (SCI)

Measures how strongly a hero rewards mastery and high-level optimization.

Higher values indicate strong scaling with player skill.

---

## Skill Floor Index (SFI)

Measures accessibility and lower-rank effectiveness.

Higher values indicate heroes that provide reliable value with less mastery required.

---

## Skill Variance Index (SVI)

Measures the gap between skill floor and skill ceiling behavior.

Higher values indicate stronger performance divergence across skill tiers.

---

# Methodology

Most composite metrics were standardized using z-score normalization:

Z = (x - μ) / σ

Where:

* x = current hero value
* μ = population average
* σ = standard deviation

This allows all indices to be interpreted relative to the overall hero population:

* positive values indicate above-average characteristics
* negative values indicate below-average characteristics
* values near zero indicate relatively average behavior

The objective of the analysis is not to determine absolute hero strength, but rather to identify:

* relative meta influence
* balance stability
* mastery scaling
* skill dependency
* seasonal volatility

---

# Tools & Technologies

* Power BI
* DAX
* Power Query
* Statistical normalization (Z-scores)
* Data visualization
* Interactive dashboard design
* Python
* Pycharm

---

# Dataset

Dataset source:

[Overwatch 2 Statistics Dataset on Kaggle](https://www.kaggle.com/datasets/mykhailokachan/overwatch-2-statistics?resource=download)

This dataset was then cleaned using the dataCleaner python file.

---

# Key Findings

* Ana demonstrated by far the highest hero dominance showing she was a very meta hero throughout Overwatch 2. Her high balance volatility is also interesting and may be explained by the various balances to the timings of her abilities used against enemy players during Overwatch 2.
* Tracer showed the highest skill variance index, which to me showcases a very fun hero for both newcomers and veterans. A hero, like Tracer, that is both easy to learn and hard to master allows for skill flexibility and more player expression.
* Some skill variances were suprising, such as Kiriko and Sombra. This could be due to enemy players at lower ranks not being able to effectively combat what may seem as basic strategies for these heroes.
* Several heroes displayed significant divergence between low-rank and high-rank effectiveness with the main standout being Roadhog.
* Meta dominance and balance volatility do not always correlate directly, highlighting differences between popularity and stability.

---

# Caveats & Limitations

* Public datasets may not fully reflect internal matchmaking or developer telemetry systems.
* Pick rate may reflect hero popularity rather than objective strength.
* Professional play and coordinated team environments may produce different results from ladder data.
* Metrics are comparative and standardized relative to the currently selected hero pool and filters.

---

# Project Purpose

This project was created to demonstrate:

* analytical problem solving
* KPI engineering
* statistical normalization
* dashboard UX design
* interactive storytelling
* advanced Power BI development

through the lens of competitive game balance analytics.
