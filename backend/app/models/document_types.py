
#app/models/document_types.py
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field

class DocumentType(str, Enum):
    """Enumeration of document types with detailed descriptions for document classification"""
    
    UNDEFINED = "Undefined"
    INVOICE = "Invoice"
    DELIVERY_NOTE = "Delivery Note"
    PURCHASE_ORDER = "Purchase Order"
    BANK_STATEMENT = "Bank Statement"
    FIXED_ASSET_SCHEDULE = "Fixed Asset Schedule"
    GENERAL_LEDGER = "General Ledger"
    BOARD_MEETING_MINUTES = "Board Meeting Minutes"
    LOAN_AGREEMENT = "Loan Agreement"
    LEASE_CONTRACT = "Lease Contract"
    INSURANCE_POLICY = "Insurance Policy"
    LEGAL_CONFIRMATION_LETTER = "Legal Confirmation Letter"
    CUSTOMER_CONTRACT = "Customer Contract"
    SHARE_PURCHASE_AGREEMENT = "Share Purchase Agreement"
    ANNUAL_REPORT = "Annual Report"
    TAX_RETURN = "Tax Return"
    CSRD_REPORT = "CSRD Report"
    PROSPECTUS = "Prospectus"
    MDA = "MD&A"
    SOC_REPORT = "SOC Report"
    MANAGEMENT_REPORT = "Management Report"
    EMPLOYMENT_CONTRACT = "Employment Contract"
    JOINT_VENTURE_AGREEMENT = "Joint Venture Agreement"
    ROYALTY_AGREEMENT = "Royalty Agreement"
    LICENSING_AGREEMENT = "Licensing Agreement"
    PENSION_REPORT = "Pension Report"
    PENSION_APPRAISAL = "Pension Appraisal"
    SHAREHOLDER_AGREEMENT = "Shareholder Agreement"
    
class DocumentClassification(BaseModel):
    """
    Model for document classification results with detailed field descriptions
    """
    type: DocumentType = Field(
        description="""
        The classified document type. Each type has specific characteristics:
        - Invoice: A commercial document issued by a seller to a buyer, listing goods/services provided and payment terms
        - Delivery Note: A document accompanying shipped goods, detailing items delivered
        - Purchase Order: A formal document from buyer to seller initiating a trade transaction
        - Bank Statement: A financial record showing account transactions over a period
        - Fixed Asset Schedule: A detailed listing of company's long-term tangible assets
        - General Ledger: The main accounting record of a business's financial transactions
        - Board Meeting Minutes: Official record of proceedings and decisions made in board meetings
        - Loan Agreement: Legal document outlining terms and conditions of a loan
        - Lease Contract: Agreement between lessor and lessee for use of property/asset
        - Insurance Policy: Contract detailing insurance coverage terms and conditions
        - Legal Confirmation Letter: Formal correspondence confirming legal matters/status
        - Customer Contract: Agreement between business and customer for products/services
        - Share Purchase Agreement: Contract for the sale and purchase of company shares
        - Annual Report: Comprehensive report on company's activities and financial performance
        - Tax Return: Official declaration of income, deductions, and tax obligations
        - CSRD Report: Corporate Sustainability Reporting Directive compliance document
        - Prospectus: Formal document providing details about an investment offering
        - MD&A: Management Discussion and Analysis of company performance
        - SOC Report: Service Organization Control audit report
        - Management Report: Internal document analyzing business performance
        - Employment Contract: Agreement between employer and employee
        - Joint Venture Agreement: Contract between parties for joint business venture
        - Royalty Agreement: Contract governing payment for use of assets/IP
        - Licensing Agreement: Contract permitting use of proprietary rights
        - Pension Report: Document detailing pension fund performance and status
        - Pension Appraisal: Evaluation of pension benefits and obligations
        - Shareholder Agreement: Contract between company shareholders defining rights/obligations
        """
    )
    confidence: float = Field(
        confidence=None, 
        description="Confidence score of the classification between 0 and 1, where 1 indicates highest confidence"
    )
    reasoning: Optional[str] = Field(
        default=None,
        description="Explanation of why the document was classified as this type, including key identifying features found"
    )