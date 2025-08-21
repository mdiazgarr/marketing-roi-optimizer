import pandas as pd

def engineer_features(input_path, output_path):
    df = pd.read_csv(input_path)

    # Convertir columnas relevantes a numéricas (quita símbolos como $ o , si existen)
    num_cols = ['Clicks', 'Impressions', 'Cost', 'Conversions', 'Sale_Amount']
    for col in num_cols:
        df[col] = pd.to_numeric(df[col].astype(str).str.replace('[\$,]', '', regex=True), errors='coerce')

    # Crear nuevas métricas
    df['CTR'] = df['Clicks'] / df['Impressions']
    df['CPC'] = df['Cost'] / df['Clicks']
    df['CPA'] = df['Cost'] / df['Conversions']
    df['ROI'] = df['Sale_Amount'] / df['Cost']

    # Limpiar NaNs e infinitos (por divisiones entre cero)
    df.replace([float('inf'), -float('inf')], pd.NA, inplace=True)
    df.dropna(subset=['CTR', 'CPC', 'CPA', 'ROI'], inplace=True)

    df.to_csv(output_path, index=False)
    print(f"✅ Feature engineering completa. Guardado en: {output_path}")

# Ejecutar script
if __name__ == "__main__":
    engineer_features('data/raw/GoogleAds_Data.csv', 'data/processed/engineered.csv')
