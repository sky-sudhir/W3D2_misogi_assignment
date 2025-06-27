'use client';

import { useState, useRef } from 'react';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Card, CardHeader, CardTitle, CardDescription, CardContent, CardFooter } from '@/components/ui/card';
import { Label } from '@/components/ui/label';
import { Loader2, Upload, Image as ImageIcon } from 'lucide-react';

export default function Home() {
  const [image, setImage] = useState<File | null>(null);
  const [imagePreview, setImagePreview] = useState<string>('');
  const [question, setQuestion] = useState('');
  const [answer, setAnswer] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState('');
  const fileInputRef = useRef<HTMLInputElement>(null);

  const handleImageUpload = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file) {
      if (file.type.startsWith('image/')) {
        setImage(file);
        setImagePreview(URL.createObjectURL(file));
        setError('');
      } else {
        setError('Please upload a valid image file');
      }
    }
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!image || !question) {
      setError('Please provide both an image and a question');
      return;
    }

    setIsLoading(true);
    setError('');
    setAnswer('');
    
    try {
      const formData = new FormData();
      formData.append('question', question);
      formData.append('image', image);
      
      const response = await fetch('http://localhost:8000/ask', {
        method: 'POST',
        body: formData,
        // Don't set Content-Type header, let the browser set it with the correct boundary
      });
      
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      
      const data = await response.json();
      setAnswer(data.answer);
    } catch (err) {
      console.error('Error:', err);
      setError('Failed to process your request. Please try again.');
    } finally {
      setIsLoading(false);
    }
  };

  const triggerFileInput = () => {
    fileInputRef.current?.click();
  };

  return (
    <main className="min-h-screen bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-4xl mx-auto">
        <div className="text-center mb-8">
          <h1 className="text-4xl font-bold text-gray-900 mb-2">Multimodal QA Agent</h1>
          <p className="text-lg text-gray-600">Ask questions about your images using AI</p>
        </div>

        <Card className="w-full">
          <CardHeader>
            <CardTitle>Upload an Image</CardTitle>
            <CardDescription>
              Upload an image and ask questions about its contents
            </CardDescription>
          </CardHeader>
          <form onSubmit={handleSubmit}>
            <CardContent className="space-y-6">
              <div className="grid w-full items-center gap-4">
                <div className="flex flex-col space-y-1.5">
                  <Label htmlFor="image">Image</Label>
                  <input
                    type="file"
                    id="image"
                    ref={fileInputRef}
                    onChange={handleImageUpload}
                    accept="image/*"
                    className="hidden"
                    disabled={isLoading}
                  />
                  <div 
                    onClick={triggerFileInput}
                    className={`flex flex-col items-center justify-center border-2 border-dashed rounded-lg p-8 cursor-pointer hover:bg-gray-50 transition-colors ${
                      isLoading ? 'opacity-50 cursor-not-allowed' : ''
                    }`}
                  >
                    {imagePreview ? (
                      <div className="relative w-full h-64">
                        <img 
                          src={imagePreview} 
                          alt="Preview" 
                          className="w-full h-full object-contain rounded-md"
                        />
                      </div>
                    ) : (
                      <>
                        <Upload className="h-12 w-12 text-gray-400 mb-2" />
                        <p className="text-sm text-gray-500">
                          Click to upload an image or drag and drop
                        </p>
                        <p className="text-xs text-gray-400 mt-1">
                          PNG, JPG, GIF up to 10MB
                        </p>
                      </>
                    )}
                  </div>
                </div>


                <div className="flex flex-col space-y-1.5">
                  <Label htmlFor="question">Your Question</Label>
                  <Input
                    id="question"
                    placeholder="What would you like to know about this image?"
                    value={question}
                    onChange={(e) => setQuestion(e.target.value)}
                    disabled={isLoading}
                  />
                </div>

                {error && (
                  <div className="text-red-500 text-sm">
                    {error}
                  </div>
                )}

                {answer && (
                  <div className="mt-4 p-4 bg-gray-50 rounded-lg border border-gray-200">
                    <h3 className="font-medium text-gray-900 mb-2">Answer:</h3>
                    <p className="text-gray-700">{answer}</p>
                  </div>
                )}
              </div>
            </CardContent>
            <CardFooter className="flex justify-end">
              <Button 
                type="submit" 
                disabled={!image || !question || isLoading}
                className="w-full sm:w-auto"
              >
                {isLoading ? (
                  <>
                    <Loader2 className="mr-2 h-4 w-4 animate-spin" />
                    Processing...
                  </>
                ) : (
                  'Ask Question'
                )}
              </Button>
            </CardFooter>
          </form>
        </Card>

        <div className="mt-8 text-center text-sm text-gray-500">
          <p>Powered by Next.js and shadcn/ui. This is a demo with simulated responses.</p>
        </div>
      </div>
    </main>
  );
}
