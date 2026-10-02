import Foundation
import PDFKit
import Vision
import AppKit
let inputs = CommandLine.arguments.dropFirst()
for file in inputs {
 guard let doc=PDFDocument(url:URL(fileURLWithPath:file)) else { continue }
 var pages:[[String:Any]]=[]
 for index in 0..<doc.pageCount {
  autoreleasepool {
   guard let page=doc.page(at:index) else{return}
   let existing=page.string ?? ""
   var text=existing
   var ocr=false
   if existing.trimmingCharacters(in:.whitespacesAndNewlines).count < 80 {
    let image=page.thumbnail(of:NSSize(width:1700,height:2200),for:.mediaBox)
    var rect=CGRect(origin:.zero,size:image.size)
    if let cg=image.cgImage(forProposedRect:&rect,context:nil,hints:nil) {
     let request=VNRecognizeTextRequest()
     request.recognitionLevel = .accurate
     request.usesLanguageCorrection = true
     request.recognitionLanguages=["en-US"]
     do {try VNImageRequestHandler(cgImage:cg).perform([request]);text=(request.results ?? []).sorted {a,b in a.boundingBox.midY > b.boundingBox.midY}.compactMap {$0.topCandidates(1).first?.string}.joined(separator:"\n");ocr=true} catch {text=""}
    }
   }
   pages.append(["page":index+1,"text":text,"ocr":ocr])
  }
 }
 let output:[String:Any]=["file":file,"pages":pages]
 if let data=try? JSONSerialization.data(withJSONObject:output),let s=String(data:data,encoding:.utf8){print(s)}
}
