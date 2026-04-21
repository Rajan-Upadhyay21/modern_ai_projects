handoff_document = {
    "model_name": "customer_churn_model",
    "version": "v3",
    "owner_team": "ml_platform_team",
    "deployment_target": "staging_api",
    "required_features": ["customer_age", "last_purchase_amount", "preferred_category"],
    "notes": "Model approved after validation and drift review."
}

print("Deployment Handoff Information:")
for key, value in handoff_document.items():
    print(f"{key}: {value}")
