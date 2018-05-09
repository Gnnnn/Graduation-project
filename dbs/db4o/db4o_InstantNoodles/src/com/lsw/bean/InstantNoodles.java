package com.lsw.bean;

public class InstantNoodles {
    public InstantNoodles() {
    }

    public InstantNoodles(Integer id, String sampleId, String name, String specification , String manufacturer) {
        super();
        this.id = id;
        this.name = name;
        this.sampleId = sampleId;
        this.specification = specification;
        this.manufacturer = manufacturer;
    }

    public InstantNoodles(Integer id) {
        super();
        this.id = id;
    }

    private java.lang.Integer id;
    private java.lang.String name;
    private java.lang.String sampleId;
    private java.lang.String specification;
    private java.lang.String manufacturer;

    public java.lang.Integer getId() {
        return id;
    }

    public void setId(java.lang.Integer id) {
        this.id = id;
    }

    public java.lang.String getName() {
        return name;
    }

    public void setName(java.lang.String name) {
        this.name = name;
    }

    public java.lang.String getSampleId() {
        return sampleId;
    }

    public void setSampleId(java.lang.String SampleId) {
        this.sampleId = SampleId;
    }
    
    public java.lang.String getSpecification() {
        return specification;
    }

    public void setSpecification(java.lang.String specification) {
        this.specification = specification;
    }
    
    public java.lang.String getManufacturer() {
        return manufacturer;
    }

    public void setManufacturer(java.lang.String manufaturer) {
        this.manufacturer = manufaturer;
    }
    
    @Override
    public String toString() {
        return "[" + id + "/" + sampleId + "/" +name + "/" + specification + "/" + manufacturer + "]";
    }

}