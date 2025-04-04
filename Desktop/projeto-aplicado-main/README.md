🌍 [Leia em Português](README.pt-BR.md)

# 📊 Applied Project - Mackenzie

Exploratory Data Analysis (EDA) about the housing conditions in the state `São Paulo (Brazil)`

## 📖 Summary

- [🎯 Objective](#-🎯-Objective)
- [📋 Dataset Details](#-📋-Dataset-Details)
- [📌 Observations](#-📌-Observations)
- [🕒 Timeline](#-🕒-Timeline)
- [🛠 Mapping Technologies](#-🛠-Mapping-Technologies)
- [💫 Steps to run](#-💫-Steps-to-run)
- [👥 Team](#-👥-Team)

## 🎯 Objective

Exploratory Data Analysis (EDA) applied to the data of housing conditions in the state of Sao Paulo, provided by the SEADE Foundation. The research involves the definition of the organizational context, characterization of the problem, selection and treatment of the database, and presentation of insights with storytelling based on the results obtained

## 📋 Dataset Details

- `cd_sector` - Industry code (a unique identification for each sector).
- `cd_dist` - District code (represents the state region).
- `nm_dist` - District name (state name).
- `area_km2` - Area of the sector in square kilometres.
- `cd_mun` - Municipality code (State code).
- `nm_mun` - Name of municipality(Name of State).
- `v0001` - Total population of the sector.
- `v0002` - Resident population in private households.
- `v0003` - Resident population in permanent private households.
- `v0004` - Resident population in improvised private households.
- `v0005` - Population density (population per km²).
- `v0006` - Percentage of households with garbage collection.
- `v0007` - Total number of households in the sector.
- `lat` - Latitude of sector location.
- `long` - Longitude of sector location.

## 📌 Observations

The dataset contains geographic data (latitude and longitude) that can be used to map the geographic distribution of different areas of Adamantina.
The area of each sector is presented in square kilometers, which allows you to calculate the population density or perform other spatial analyzes.

## 🕒 Timeline

- `Week 1` - Data collection and organization.
- `Week 2` - Exploratory analysis and identification of patterns.
- `Week 3` - Construction of visualizations and reports.
- `Week 4` - Review, final adjustments and submission of the report.

## 🛠 Mapping Technologies

Mapping of possible technologies that can be used for data analysis and visualization:

- 📊 `pandas` - Data manipulation and analysis.
- 📈 `matplotlib` - Creating graphs and data visualizations.
- 🤖 `scikit-learn` - Development of predictive models (if necessary).
- 🖥 `streamlit` - Construction of interactive dashboards to visualize results.

## 💫 Steps to run

1. Clone the repository:

```bash
git clone https://github.com/felipeclarindo/projeto-aplicado.git
```

2. Enter directory:

```bash
cd projeto-aplicado
```

3. Create an `Virtual Environment`:

```bash
python -m venv .venv
```

4. Run the `Activate.bat` file located at `.venv/Scripts/Activate.bat`. (Then type `cd ..` until you are back to root.)

5. Install the dependencies:

```bash
pip install -r ./requirements.txt
```

6. Run the cell from the jupyter file (`projeto_aplicado.ipynb`) located in the `src/´projeto_aplicado.ipynb`.

## 👥 Team

- [Felipe Clarindo](https://github.com/felipeclarindo)
- [Victoria Fontes](https://github.com/victoriafortes)
- [Alexandre Zamarion](https://github.com/alezamarion)
