from pydantic import BaseModel, Field


class OptimizeRequest(BaseModel):
    project_name: str = Field(..., min_length=2, max_length=100)
    material: str = Field(..., min_length=3, max_length=50)
    quantity: int = Field(..., gt=0)
    budget: float = Field(..., gt=0)
    carbon_limit: float = Field(..., gt=0)


class SupplierAllocation(BaseModel):
    supplier: str
    units: int
    unit_cost: float
    unit_carbon: float
    total_cost: float
    total_carbon: float


class OptimizeResponse(BaseModel):
    project_name: str
    material: str
    recommended_supplier: str
    supplier_mix: list[SupplierAllocation]
    total_units: int
    optimized_cost: float
    optimized_carbon: float
    carbon_limit: float
    carbon_savings_percent: float
    budget_remaining: float
    recommendation: str
