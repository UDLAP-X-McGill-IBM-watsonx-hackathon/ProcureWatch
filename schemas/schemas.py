class DocumentClassification(BaseModel):
    document_type: Literal['contract', 'invoice', 'email', 'meeting_minutes', 'receipt', 'unknown']
    confidence: float
    reasoning: str

class Invoice(BaseModel):
    document_type: Literal['invoice'] = 'invoice'
    client_name: Optional[str] = None
    invoice_number: Optional[str] = None
    invoice_amount: Optional[str] = None
    invoice_date: Optional[str] = None
    vendor_name: Optional[str] = None
    line_items: List[str] = Field(default_factory=list)
    payment_method: Optional[str] = None
    tax_amount: Optional[str] = None

class Receipt(BaseModel):
    document_type: Literal['receipt'] = 'receipt'
    vendor_name: Optional[str] = None
    receipt_date: Optional[str] = None
    total_amount: Optional[str] = None
    payment_method: Optional[str] = None
    line_items: List[str] = Field(default_factory=list)
    tax_amount: Optional[str] = None
    tip_amount: Optional[str] = None